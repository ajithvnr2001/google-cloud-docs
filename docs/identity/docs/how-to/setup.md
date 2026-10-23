---
url: https://docs.cloud.google.com/identity/docs/how-to/setup/
title: Setting up the Groups API \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:38.208545+00:00
---

# Setting up the Groups API  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Setting up the Groups API

This page explains how to set up the Cloud Identity Groups API.

**Note:** To use the Groups API, you must have Google Groups for Business enabled for your domain and allow end users to create groups. See [Turn Groups for Business ON or OFF](https://support.google.com/a/answer/167096?ref_topic=9400092) and [Set Groups for Business sharing options](https://support.google.com/a/answer/9400084) for more information. These steps require Google Workspace administrator access to your domain.

## Before you begin

Enable the Cloud Identity API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudidentity.googleapis.com)

## Installing the client libraries

To install the client libraries, run the following command:

###  Python 

For more on setting up your Python development environment, refer to the [Python Development Environment Setup Guide](https://docs.cloud.google.com/python/docs/setup).
    
    
    pip install --upgrade google-api-python-client google-auth \
      google-auth-oauthlib google-auth-httplib2
    

## Authenticating with the Groups API

You can authenticate with the Groups API as an end user, as a service account group admin without domain-wide delegation, or as a service account with domain-wide delegation. The following sections describe each method.

### Authenticating as an end user

If you're not an administrator, or are building an app that acts on behalf of users who aren't administrators, see [Using OAuth 2.0 for web server applications](https://developers.google.com/identity/protocols/oauth2/web-server), and then see the Instantiating a client section below.

### Authenticating as a service account without domain-wide delegation

If you're using a service account and want to use it to manage groups as a group admin, complete the steps below. This authentication method should be used when you want the service account's actions to be registered in the audit logs as the service account.

#### Assigning an admin role to the service account

**Tip:** If the service account doesn't need access to all of the groups, consider making it an owner of the groups of interest. You don't need to assign the group admin role in this case.

First, you should assign the Google Workspace Group Administrator Role (Group Administrator) to the service account you want to delegate to, using the Admin SDK Roles and Role Assignments API. This step gives the service account access to the groups of the domain but no other resource.

**Note:** You must have Google Workspace Super Admin access for your domain to make the service account a delegated admin.

See the [Managing Roles guide](https://developers.google.com/admin-sdk/directory/v1/guides/manage-roles) for general information about managing Roles using the Admin SDK API. Follow the steps below to assign the Group Adminstrator role for your service account.

  1. In the Google Cloud console, go to the **Service Accounts** page:

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click the name of the service account that you want to use with the Groups API.

  3. Copy the **Unique ID** of the service account.

  4. Call the Admin SDK Roles API to identify the `roleId` for Group Administrator. You can use the [API Explorer](https://developers.google.com/admin-sdk/directory/v1/reference/roles/list?apix_params=%7B%22customer%22%3A%22my_customer%22%7D&apix=true) in the Admin SDK documentation to do this.

  5. Call the [Role Assignments API](https://developers.google.com/admin-sdk/directory/v1/reference/roleAssignments/insert) with the following request body:
         
         {
           "assignedTo": "SERVICE_ACCOUNT_UNIQUE_ID"
           "roleId": "ROLE_ID"
           "scopeType": "CUSTOMER"
           "kind": "admin#directory#roleAssignment"
         }
         




#### Authenticating and authorizing the service account

You now have a service account with the Group Administrator role. The second step is to complete the OAuth authentication process for the service account.

  * If you are developing an app on Google Cloud and the service account is an owner of the project, you can use the application default credentials instead, which can simplify the process. See [Authenticating as a Service Account](https://docs.cloud.google.com/docs/authentication/production#passing_code) for more information.

  * If the service account is not the owner of the project, follow the instructions below.




In either case, the applicable scope for the Cloud Identity Groups API is `https://www.googleapis.com/auth/cloud-identity.groups`.

  1. Using the credential you just created, generate an access token.

**Note:** Do not impersonate a user when generating credentials. Skip fields such as `with_subject`, `createDelegated`, or `setServiceAccountUser`.

###  Java 
         
         GoogleCredential credential = new GoogleCredential.Builder()
             .setTransport(httpTransport)
             .setJsonFactory(JSON_FACTORY)
             .setServiceAccountId(emailAddress)
             .setServiceAccountPrivateKeyFromP12File(new File("MyProject.p12"))
             .setServiceAccountScopes(ImmutableList.of("https://www.googleapis.com/auth/cloud-identity.groups"))
             .build();
         

###  Python 
         
         from google.oauth2 import service_account
         
         SCOPES = ['https://www.googleapis.com/auth/cloud-identity.groups']
         SERVICE_ACCOUNT_FILE = '/path/to/service-account-file.json'
         
         credentials = service_account.Credentials.from_service_account_file(
             SERVICE_ACCOUNT_FILE, scopes=SCOPES)
         

###  Go 
         
         import (
                 "context"
                 "os"
         
                 "golang.org/x/oauth2/google"
         )
         
         ctx := context.Background()
         jsonKey, err := os.ReadFile("/path/to/service-account-file.json")
         if err != nil {
                 // Handle error.
         }
         conf, err := google.JWTConfigFromJSON(jsonKey, "https://www.googleapis.com/auth/cloud-identity.groups")
         if err != nil {
                 // Handle error.
         }
         ts := conf.TokenSource(ctx)
         

Keep the access token that's generated.




**Full code for generating an access token for a service account**

###  Java 

GenerateServiceAccountOauth2Token.java
    
    
    package com.google.tools;
    
    import com.google.api.client.googleapis.auth.oauth2.[GoogleCredential](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential.html);
    import com.google.api.client.http.[HttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.common.collect.ImmutableList;
    import java.io.FileInputStream;
    
    /** Command line tool to generate Oauth2 token for a given service account
    /** without domain wide delegation. */
    public final class GenerateServiceAccountOauth2Token {
    
      private static final ImmutableList<String> API_SCOPES =
          ImmutableList.of(
              "https://www.googleapis.com/auth/cloud-identity.groups",
              "https://www.googleapis.com/auth/admin.directory.group",
              "https://www.googleapis.com/auth/admin.directory.group.member",
              "https://www.googleapis.com/auth/apps.groups.settings");
    
      public static void main(final String[] args) throws Exception {
        String accessToken = getTokenFromJsonKey();
        System.out.println("Token: " + accessToken);
      }
    
      private static String getTokenFromJsonKey() throws Exception {
        [GoogleCredential](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential.html) credential =
            [GoogleCredential](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential.html).[fromStream](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential.html#com_google_api_client_googleapis_auth_oauth2_GoogleCredential_fromStream_java_io_InputStream_)(
                new FileInputStream(
                    "<path for json file>"),
                new [NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html)(),
                [GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html).getDefaultInstance());
        System.out.println("ServiceAccountId=" + credential.[getServiceAccountId](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential.html#com_google_api_client_googleapis_auth_oauth2_GoogleCredential_getServiceAccountId__)());
    
        [HttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport.html) httpTransport = new [NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html)();
        [JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html) jsonFactory = [GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html).getDefaultInstance();
        [GoogleCredential](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential.html).Builder builder =
            new [GoogleCredential](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential.html).Builder()
                .[setServiceAccountPrivateKey](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential.Builder.html#com_google_api_client_googleapis_auth_oauth2_GoogleCredential_Builder_setServiceAccountPrivateKey_java_security_PrivateKey_)(credential.[getServiceAccountPrivateKey](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential.html#com_google_api_client_googleapis_auth_oauth2_GoogleCredential_getServiceAccountPrivateKey__)())
                .[setServiceAccountPrivateKeyId](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential.Builder.html#com_google_api_client_googleapis_auth_oauth2_GoogleCredential_Builder_setServiceAccountPrivateKeyId_java_lang_String_)(credential.[getServiceAccountPrivateKeyId](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential.html#com_google_api_client_googleapis_auth_oauth2_GoogleCredential_getServiceAccountPrivateKeyId__)())
                .[setServiceAccountId](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential.Builder.html#com_google_api_client_googleapis_auth_oauth2_GoogleCredential_Builder_setServiceAccountId_java_lang_String_)(credential.[getServiceAccountId](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential.html#com_google_api_client_googleapis_auth_oauth2_GoogleCredential_getServiceAccountId__)())
                .setTransport(httpTransport)
                .setJsonFactory(jsonFactory)
                .[setServiceAccountScopes](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleCredential.Builder.html#com_google_api_client_googleapis_auth_oauth2_GoogleCredential_Builder_setServiceAccountScopes_java_util_Collection_java_lang_String__)(API_SCOPES)
                .setClock(credential.getClock());
        credential = builder.build();
        if (!credential.refreshToken()) {
          throw new Exception("Failed to fetch access token.");
        }
        return credential.getAccessToken();
      }
    }
    
    

Build rule
    
    
    java_binary(
      name = "generate_oauth2_token",
      srcs = ["GenerateServiceAccountOauth2Token.java"],
      main_class = "com.google.tools.GenerateServiceAccountOauth2Token",
      deps = [
          "//java/com/google/api/client/googleapis/auth/oauth2",
          "//java/com/google/api/client/googleapis/javanet",
          "//java/com/google/api/client/http",
          "//java/com/google/api/client/http/javanet",
          "//java/com/google/common/base",
          "//java/com/google/common/collect",
          "//third_party/java/google_http_java_client:gson",
          "//third_party/java/google_http_java_client:json",
      ],
    )
    
    

#### Testing the service account

  1. Try any Groups API call with the service account credentials: create a group, add users, update group settings, etc.

  2. Check the Audit Logs in the Google Admin Console Reports section. You should see the service account as the actor for your group-related changes. See [Log events](https://support.google.com/a/answer/6098211) for more information.

Alternatively, you can use APIs to access audit logs. To check using the [Reports API explorer](https://developers.google.com/admin-sdk/reports/v1/reference/activities/list), make sure to use your admin OAuth credentials.




### Authenticating as a service account with domain-wide delegation

If you're an administrator managing identity groups, or if you want to provide an account with domain-wide privileges so it can manage Google Groups on behalf of admins, you should authenticate as a [service account](https://docs.cloud.google.com/iam/docs/service-accounts).

**Note:** Because domain-wide delegation works by allowing the service account to impersonate an admin user, audit logs will show any service account actions as the user. If you want the actions to show up as the service account, see Authenticating as a service account without domain-wide-delegation above.

For details about setting up domain-wide delegation, see [Control API access with domain-wide delegation](https://support.google.com/a/answer/162106).

To authenticate as a service account, refer to [Using OAuth 2.0 for server to server applications](https://developers.google.com/identity/protocols/oauth2/service-account). When initializing the credential in your code, specify the email address on which the service account acts by calling `with_subject()` on the credential. For example:

###  Java 
    
    
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    
    [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html) credentials = [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html)
        .fromStream(new FileInputStream(SERVICE_ACCOUNT_FILE))
        .createScoped(SCOPES)
        .createDelegated(delegated_email);
    

###  Python 
    
    
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES).with_subject(delegated_email)
    

###  Go 
    
    
    import (
            "context"
            "os"
    
            "golang.org/x/oauth2/google"
    )
    
    ctx := context.Background()
    jsonKey, err := os.ReadFile(SERVICE_ACCOUNT_FILE)
    if err != nil {
            // Handle error.
    }
    config, err := google.JWTConfigFromJSON(jsonKey, SCOPES...)
    if err != nil {
            // Handle error.
    }
    config.Subject = delegated_email
    ts := config.TokenSource(ctx)
    

#### Instantiating a client

The following example shows how to instantiate a client using service account credentials. To authenticate as an end-user instead, replace the `credential` object from the service account with the `credential` you obtained earlier in [Using OAuth 2.0 for web server applications](https://developers.google.com/identity/protocols/oauth2/web-server#obtainingaccesstokens).

###  Java 
    
    
    import com.google.api.client.googleapis.javanet.[GoogleNetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.javanet.GoogleNetHttpTransport.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.cloudidentity.v1.CloudIdentity;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    
    import java.io.FileInputStream;
    import java.util.Collections;
    import java.util.List;
    
    // ...
    
    List<String> SCOPES = Collections.singletonList("https://www.googleapis.com/auth/cloud-identity.groups");
    String SERVICE_ACCOUNT_FILE = "/path/to/service-account-file.json";
    
    public CloudIdentity createService() throws Exception {
      [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html) credentials = [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html)
          .fromStream(new FileInputStream(SERVICE_ACCOUNT_FILE))
          .createScoped(SCOPES)
          .createDelegated("user@example.org"); // Omit for no domain-wide delegation
    
      CloudIdentity service = new CloudIdentity.Builder(
          [GoogleNetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.javanet.GoogleNetHttpTransport.html).[newTrustedTransport](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.javanet.GoogleNetHttpTransport.html#com_google_api_client_googleapis_javanet_GoogleNetHttpTransport_newTrustedTransport__)(),
          [GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html).[getDefaultInstance](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html#com_google_api_client_json_gson_GsonFactory_getDefaultInstance__)(),
          new [HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html)(credentials))
          .setApplicationName("your-app-name")
          .build();
    
      return service;
    }
    

###  Python 
    
    
    from google.oauth2 import service_account
    import googleapiclient.discovery
    
    SCOPES = ['https://www.googleapis.com/auth/cloud-identity.groups']
    SERVICE_ACCOUNT_FILE = '/path/to/service-account-file.json'
    
    def create_service():
      credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
      delegated_credentials = credentials.with_subject('user@example.org') # Omit for no domain-wide delegation
    
      service_name = 'cloudidentity'
      api_version = 'v1'
      service = googleapiclient.discovery.build(
        service_name,
        api_version,
        credentials=delegated_credentials)
    
      return service
    

###  Go 
    
    
    import (
            "context"
            "os"
    
            "golang.org/x/oauth2/google"
            "google.golang.org/api/cloudidentity/v1"
            "google.golang.org/api/option"
    )
    
    // ...
    
    scopes := []string{"https://www.googleapis.com/auth/cloud-identity.groups"}
    serviceAccountFile := "/path/to/service-account-file.json"
    
    func createService(ctx context.Context) (*cloudidentity.Service, error) {
            jsonKey, err := os.ReadFile(serviceAccountFile)
            if err != nil {
                    return nil, err
            }
            config, err := google.JWTConfigFromJSON(jsonKey, scopes...)
            if err != nil {
                    return nil, err
            }
            config.Subject = "user@example.org" // Omit for no domain-wide delegation
            ts := config.TokenSource(ctx)
    
            service, err := cloudidentity.NewService(ctx, option.WithTokenSource(ts))
            return service, err
    }
    

You can now begin making calls to the Groups API.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
