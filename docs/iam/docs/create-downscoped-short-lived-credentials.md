---
url: https://docs.cloud.google.com/iam/docs/create-downscoped-short-lived-credentials/
title: Create a downscoped short-lived credential \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:30:58.704457+00:00
---

# Create a downscoped short-lived credential  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/create-downscoped-short-lived-credentials/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Create a downscoped short-lived credential Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use Credential Access Boundaries to create an OAuth 2.0 access token with downscoped Cloud Storage permissions.

The process for creating a token with downscoped permissions includes the following steps:

  1. Grant the appropriate IAM roles to a user or service account.
  2. Define a Credential Access Boundary that sets an upper bound on the permissions that are available to the user or service account.
  3. Create an OAuth 2.0 access token for the user or service account.
  4. Exchange the OAuth 2.0 access token for a new token that respects the Credential Access Boundary.



You can then use the new downscoped OAuth 2.0 access token to authenticate requests to Cloud Storage.

## Before you begin

Before you use Credential Access Boundaries, make sure you meet the following requirements:

  * You need to downscope permissions only for Cloud Storage, not for other Google Cloud services.

If you need to downscope permissions for additional Google Cloud services, you can create multiple [service accounts](https://docs.cloud.google.com/iam/docs/service-accounts) and grant a different set of roles to each service account.

  * You can use [OAuth 2.0 access tokens](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials#sa-credentials-oauth) for authentication. Other types of short-lived credentials don't support Credential Access Boundaries.




Also, you must enable the required APIs:

  * Enable the IAM and Security Token Service APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com,sts.googleapis.com&redirect=https%3A//console.cloud.google.com)




## Grant IAM roles

A Credential Access Boundary sets an upper bound on the available permissions for a resource. It can subtract permissions from a principal, but it can't add permissions that the principal does not already have.

As a result, you must also grant roles to the principal that provide the permissions they need, either [on a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add) or [on a higher-level resource](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access), such as the project.

For example, suppose you need to create a downscoped short-lived credential that allows a service account to create objects in a bucket:

  * At a minimum, you must grant a role to the service account that includes the `storage.objects.create` permission, such as the Storage Object Creator role (`roles/storage.objectCreator`). The Credential Access Boundary must also include this permission.
  * You can also grant a role that includes more permissions, such as the Storage Object Admin role (`roles/storage.objectAdmin`). The service account can use only the permissions that appear in both the role grant and the Credential Access Boundary.



To learn about predefined roles for Cloud Storage, see [Cloud Storage roles](https://docs.cloud.google.com/iam/docs/roles-permissions/storage).

## Define the Credential Access Boundary

A Credential Access Boundary is an object that contains a list of _access boundary rules_. The rules are made up of parameters that specify the upper bound of the permissions that are available to the user or service account. To define a Credential Access Boundary, create a JSON object that lists the access boundary rules and their parameters.

The following is an example of a Credential Access Boundary:
    
    
    {
      "accessBoundary": {
        "accessBoundaryRules": [
          {
            "availablePermissions": [
              "inRole:ROLE_ID"
            ],
            "availableResource": "//storage.googleapis.com/projects/_/buckets/BUCKET_NAME"
             "availabilityCondition": {
                "expression" : "CONDITION"
          }
        ]
      }
    }
    

Replace the following:

  * `ROLE_ID`: The ID of a predefined or custom role that defines the upper bound on the available permissions for the resource. For example, `roles/storage.objectViewer`. To specify multiple roles, add a new line with an `inRole:` prefix followed by the role ID. Only the permissions in the specified roles will be available.
  * `BUCKET_NAME`: The name of the Cloud Storage bucket that the rule applies to.
  * `CONDITION`: Optional. A condition expression that specifies the Cloud Storage objects where permissions are available. For example, the following condition makes permissions available for objects whose name starts with `customer-a`:
        
        resource.name.startsWith('projects/_/buckets/example-bucket/objects/customer-a')
        




To learn more about how to create and customize credential access boundaries, see [Components of a Credential Access Boundary](https://docs.cloud.google.com/iam/docs/downscoping-short-lived-credentials#define-boundary).

For examples of potential use cases for Credential Access Boundaries, see [Examples of Credential Access Boundaries](https://docs.cloud.google.com/iam/docs/downscoping-short-lived-credentials#examples).

## Create an OAuth 2.0 access token

Before you create a downscoped short-lived credential, you must create a normal OAuth 2.0 access token. You can then exchange the normal credential for a downscoped credential. When you create the access token, use the OAuth 2.0 scope `https://www.googleapis.com/auth/cloud-platform`.

To create an access token for a service account, you can [complete the server-to-server OAuth 2.0 flow](https://developers.google.com/identity/protocols/OAuth2ServiceAccount), or you can use the Service Account Credentials API to [generate an OAuth 2.0 access token](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials#sa-credentials-oauth).

To create an access token for a user, see [Obtaining OAuth 2.0 access tokens](https://developers.google.com/identity/protocols/OAuth2WebServer#obtainingaccesstokens). You can also use the [OAuth 2.0 Playground](https://developers.google.com/oauthplayground/) to create an access token for your own Google Account.

## Exchange the OAuth 2.0 access token

After you create an OAuth 2.0 access token, you can exchange the access token for a downscoped token that respects the Credential Access Boundary. This process typically involves a _token broker_ and a _token consumer_ :

  * The _token broker_ is responsible for defining the Credential Access Boundary and exchanging an access token for a downscoped token.

The token broker can use a supported authentication library to exchange access tokens automatically, or it can call the Security Token Service to exchange tokens manually.

  * The _token consumer_ requests a downscoped access token from the token broker, then uses the downscoped access token to perform another action.

The token consumer can use a supported authentication library to automatically refresh access tokens before they expire. Alternatively, it can refresh tokens manually, or it can allow tokens to expire without refreshing them.




There are two ways to exchange the access token for a downscoped token:

  * **Client-side token exchange (recommended)** : Clients obtain cryptographic materials from the Security Token Service API server. The cryptographic materials allow clients to generate downscoped tokens with varying Credential Access Boundary rules independently on the client side for a set duration (for example, 1 hour). This approach reduces latency and improves efficiency, especially for clients requiring frequent Credential Access Boundary rule updates. It's also more efficient for applications that need to generate many unique downscoped tokens. This is the recommended approach because it provides better performance, scalability, and future feature compatibility.

  * **Server-side token exchange** : Clients request a new downscoped token from the Security Token Service API server whenever a Credential Access Boundary rule changes. This approach is straightforward but requires a round trip to the Security Token Service API server for each downscoped token request. This approach is recommended only for customers who require a client library that doesn't support client-side token exchange, due to the round trip to the Security Token Service API for each downscoped token request.




### Client-side token exchange

If you create the token broker and token consumer with the following language, you can use Google's authentication library to exchange and refresh tokens automatically through the client-side approach.

### Java

For Java, you can exchange and refresh tokens automatically with version 1.32.1 or later of the [`com.google.auth:google-auth-library-cab-token-generator` artifact](https://search.maven.org/artifact/com.google.auth/google-auth-library-oauth2-http).

To check your artifact version, run the following Maven command in your application directory:
    
    
    mvn dependency:list -DincludeArtifactIds=google-auth-library-cab-token-generator
    

The following example shows how a token broker can generate downscoped tokens:
    
    
    import com.google.auth.credentialaccessboundary.[ClientSideCredentialAccessBoundaryFactory](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.credentialaccessboundary.ClientSideCredentialAccessBoundaryFactory.html);
    import com.google.auth.oauth2.[AccessToken](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.AccessToken.html);
    import com.google.auth.oauth2.[CredentialAccessBoundary](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.CredentialAccessBoundary.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import dev.cel.common.CelValidationException;
    import java.io.IOException;
    import java.security.GeneralSecurityException;
      public static [AccessToken](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.AccessToken.html) getTokenFromBroker(String bucketName, String objectPrefix)
          throws IOException {
        // Retrieve the source credentials from ADC.
        [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html) sourceCredentials =
            [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html).[getApplicationDefault](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html#com_google_auth_oauth2_GoogleCredentials_getApplicationDefault__)()
                .createScoped("https://www.googleapis.com/auth/cloud-platform");
    
        // Initialize the Credential Access Boundary rules.
        String availableResource = "//storage.googleapis.com/projects/_/buckets/" + bucketName;
    
        // Downscoped credentials will have readonly access to the resource.
        String availablePermission = "inRole:roles/storage.objectViewer";
    
        // Only objects starting with the specified prefix string in the object name will be allowed
        // read access.
        String expression =
            "resource.name.startsWith('projects/_/buckets/"
                + bucketName
                + "/objects/"
                + objectPrefix
                + "')";
    
        // Build the AvailabilityCondition.
        [CredentialAccessBoundary](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.CredentialAccessBoundary.html).[AccessBoundaryRule](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.CredentialAccessBoundary.AccessBoundaryRule.html).[AvailabilityCondition](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.CredentialAccessBoundary.AccessBoundaryRule.AvailabilityCondition.html) availabilityCondition =
            [CredentialAccessBoundary](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.CredentialAccessBoundary.html).AccessBoundaryRule.AvailabilityCondition.newBuilder()
                .[setExpression](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.CredentialAccessBoundary.AccessBoundaryRule.AvailabilityCondition.Builder.html#com_google_auth_oauth2_CredentialAccessBoundary_AccessBoundaryRule_AvailabilityCondition_Builder_setExpression_java_lang_String_)(expression)
                .build();
    
        // Define the single access boundary rule using the above properties.
        [CredentialAccessBoundary](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.CredentialAccessBoundary.html).[AccessBoundaryRule](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.CredentialAccessBoundary.AccessBoundaryRule.html) rule =
            [CredentialAccessBoundary](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.CredentialAccessBoundary.html).AccessBoundaryRule.newBuilder()
                .setAvailableResource(availableResource)
                .[addAvailablePermission](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.CredentialAccessBoundary.AccessBoundaryRule.Builder.html#com_google_auth_oauth2_CredentialAccessBoundary_AccessBoundaryRule_Builder_addAvailablePermission_java_lang_String_)(availablePermission)
                .[setAvailabilityCondition](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.CredentialAccessBoundary.AccessBoundaryRule.Builder.html#com_google_auth_oauth2_CredentialAccessBoundary_AccessBoundaryRule_Builder_setAvailabilityCondition_com_google_auth_oauth2_CredentialAccessBoundary_AccessBoundaryRule_AvailabilityCondition_)(availabilityCondition)
                .build();
    
        // Define the Credential Access Boundary with all the relevant rules.
        [CredentialAccessBoundary](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.CredentialAccessBoundary.html) credentialAccessBoundary =
            [CredentialAccessBoundary](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.CredentialAccessBoundary.html).newBuilder().[addRule](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.CredentialAccessBoundary.Builder.html#com_google_auth_oauth2_CredentialAccessBoundary_Builder_addRule_com_google_auth_oauth2_CredentialAccessBoundary_AccessBoundaryRule_)(rule).build();
    
        // Create an instance of ClientSideCredentialAccessBoundaryFactory.
        [ClientSideCredentialAccessBoundaryFactory](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.credentialaccessboundary.ClientSideCredentialAccessBoundaryFactory.html) factory =
            [ClientSideCredentialAccessBoundaryFactory](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.credentialaccessboundary.ClientSideCredentialAccessBoundaryFactory.html).newBuilder()
                .setSourceCredential(sourceCredentials)
                .build();
    
        // Generate the token and pass it to the Token Consumer.
        try {
          return factory.[generateToken](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.credentialaccessboundary.ClientSideCredentialAccessBoundaryFactory.html#com_google_auth_credentialaccessboundary_ClientSideCredentialAccessBoundaryFactory_generateToken_com_google_auth_oauth2_CredentialAccessBoundary_)(credentialAccessBoundary);
        } catch (GeneralSecurityException | CelValidationException e) {
          throw new IOException("Error generating downscoped token", e);
        }
      }

The following example shows how a token consumer can use a refresh handler to automatically obtain and refresh downscoped tokens:
    
    
    import com.google.auth.oauth2.[AccessToken](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.AccessToken.html);
    import com.google.auth.oauth2.[OAuth2CredentialsWithRefresh](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2CredentialsWithRefresh.html);
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.io.IOException;
      public static String retrieveBlobWithDownscopedToken(
          final String bucketName, final String objectName) throws IOException {
        // You can pass an `OAuth2RefreshHandler` to `OAuth2CredentialsWithRefresh` which will allow the
        // library to seamlessly handle downscoped token refreshes on expiration.
        [OAuth2CredentialsWithRefresh](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2CredentialsWithRefresh.html).[OAuth2RefreshHandler](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2CredentialsWithRefresh.OAuth2RefreshHandler.html) handler =
            new [OAuth2CredentialsWithRefresh](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2CredentialsWithRefresh.html).[OAuth2RefreshHandler](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2CredentialsWithRefresh.OAuth2RefreshHandler.html)() {
              @Override
              public [AccessToken](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.AccessToken.html) refreshAccessToken() throws IOException {
                // The common pattern of usage is to have a token broker pass the downscoped short-lived
                // access tokens to a token consumer via some secure authenticated channel.
                // For illustration purposes, we are generating the downscoped token locally.
                // We want to test the ability to limit access to objects with a certain prefix string
                // in the resource bucket. objectName.substring(0, 3) is the prefix here. This field is
                // not required if access to all bucket resources are allowed. If access to limited
                // resources in the bucket is needed, this mechanism can be used.
                return DownscopedAccessTokenGenerator
                    .getTokenFromBroker(bucketName, objectName);
              }
            };
    
        [AccessToken](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.AccessToken.html) downscopedToken = handler.refreshAccessToken();
    
        [OAuth2CredentialsWithRefresh](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2CredentialsWithRefresh.html) credentials =
            [OAuth2CredentialsWithRefresh](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2CredentialsWithRefresh.html).newBuilder()
                .setAccessToken(downscopedToken)
                .[setRefreshHandler](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2CredentialsWithRefresh.Builder.html#com_google_auth_oauth2_OAuth2CredentialsWithRefresh_Builder_setRefreshHandler_com_google_auth_oauth2_OAuth2CredentialsWithRefresh_OAuth2RefreshHandler_)(handler)
                .build();
    
        [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html) options = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setCredentials(credentials).build();
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = options.[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) blob = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName, objectName);
        if (blob == null) {
          return null;
        }
        return new String(blob.[getContent](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html#com_google_cloud_storage_Blob_getContent_com_google_cloud_storage_Blob_BlobSourceOption____)());
      }

### Server-side token exchange

This section describes the following methods that you can use to exchange tokens through the service side approach:

  * Exchange and refresh the access token automatically
  * Exchange and refresh the access token manually



#### Exchange and refresh the access token automatically using server-side approach

If you create the token broker and token consumer with one of the following languages, you can use Google's authentication library to exchange and refresh tokens automatically using the server-side token generation approach:

### Go

For Go, you can exchange and refresh tokens automatically with version v0.0.0-20210819190943-2bc19b11175f or later of the [`golang.org/x/oauth2` package](https://pkg.go.dev/golang.org/x/oauth2).

To check your package version, run the following command in your application directory:
    
    
    go list -m golang.org/x/oauth2
    

The following example shows how a token broker can generate downscoped tokens:
    
    
    import (
    	"context"
    	"fmt"
    
    	"golang.org/x/oauth2"
    	"golang.org/x/oauth2/google"
    	"golang.org/x/oauth2/google/downscope"
    )
    
    // createDownscopedToken would be run on the token broker in order to generate
    // a downscoped access token that only grants access to objects whose name begins with prefix.
    // The token broker would then pass the newly created token to the requesting token consumer for use.
    func createDownscopedToken(bucketName string, prefix string) error {
    	// bucketName := "foo"
    	// prefix := "profile-picture-"
    
    	ctx := context.Background()
    	// A condition can optionally be provided to further restrict access permissions.
    	condition := downscope.AvailabilityCondition{
    		Expression:  "resource.name.startsWith('projects/_/buckets/" + bucketName + "/objects/" + prefix + "')",
    		Title:       prefix + " Only",
    		Description: "Restricts a token to only be able to access objects that start with `" + prefix + "`",
    	}
    	// Initializes an accessBoundary with one Rule which restricts the downscoped
    	// token to only be able to access the bucket "bucketName" and only grants it the
    	// permission "storage.objectViewer".
    	accessBoundary := []downscope.AccessBoundaryRule{
    		{
    			AvailableResource:    "//storage.googleapis.com/projects/_/buckets/" + bucketName,
    			AvailablePermissions: []string{"inRole:roles/storage.objectViewer"},
    			Condition:            &condition, // Optional
    		},
    	}
    
    	// This Source can be initialized in multiple ways; the following example uses
    	// Application Default Credentials.
    	var rootSource oauth2.TokenSource
    
    	// You must provide the "https://www.googleapis.com/auth/cloud-platform" scope.
    	rootSource, err := google.DefaultTokenSource(ctx, "https://www.googleapis.com/auth/cloud-platform")
    	if err != nil {
    		return fmt.Errorf("failed to generate rootSource: %w", err)
    	}
    
    	// downscope.NewTokenSource constructs the token source with the configuration provided.
    	dts, err := downscope.NewTokenSource(ctx, downscope.DownscopingConfig{RootSource: rootSource, Rules: accessBoundary})
    	if err != nil {
    		return fmt.Errorf("failed to generate downscoped token source: %w", err)
    	}
    	// Token() uses the previously declared TokenSource to generate a downscoped token.
    	tok, err := dts.Token()
    	if err != nil {
    		return fmt.Errorf("failed to generate token: %w", err)
    	}
    	// Pass this token back to the token consumer.
    	_ = tok
    	return nil
    }
    

The following example shows how a token consumer can use a refresh handler to automatically obtain and refresh downscoped tokens:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"golang.org/x/oauth2/google"
    	"golang.org/x/oauth2/google/downscope"
    
    	"cloud.google.com/go/storage"
    	"golang.org/x/oauth2"
    	"google.golang.org/api/option"
    )
    
    // A token consumer should define their own tokenSource. In the Token() method,
    // it should send a query to a token broker requesting a downscoped token.
    // The token broker holds the root credential that is used to generate the
    // downscoped token.
    type localTokenSource struct {
    	ctx        context.Context
    	bucketName string
    	brokerURL  string
    }
    
    func (lts localTokenSource) Token() (*oauth2.Token, error) {
    	var remoteToken *oauth2.Token
    	// Usually you would now retrieve remoteToken, an oauth2.Token, from token broker.
    	// This snippet performs the same functionality locally.
    	accessBoundary := []downscope.AccessBoundaryRule{
    		{
    			AvailableResource:    "//storage.googleapis.com/projects/_/buckets/" + lts.bucketName,
    			AvailablePermissions: []string{"inRole:roles/storage.objectViewer"},
    		},
    	}
    	rootSource, err := google.DefaultTokenSource(lts.ctx, "https://www.googleapis.com/auth/cloud-platform")
    	if err != nil {
    		return nil, fmt.Errorf("failed to generate rootSource: %w", err)
    	}
    	dts, err := downscope.NewTokenSource(lts.ctx, downscope.DownscopingConfig{RootSource: rootSource, Rules: accessBoundary})
    	if err != nil {
    		return nil, fmt.Errorf("failed to generate downscoped token source: %w", err)
    	}
    	// Token() uses the previously declared TokenSource to generate a downscoped token.
    	remoteToken, err = dts.Token()
    	if err != nil {
    		return nil, fmt.Errorf("failed to generate token: %w", err)
    	}
    
    	return remoteToken, nil
    }
    
    // getObjectContents will read the contents of an object in Google Storage
    // named objectName, contained in the bucket "bucketName".
    func getObjectContents(output io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string, objectName string) error {
    	// bucketName := "foo"
    	// prefix := "profile-picture-"
    
    	ctx := context.Background()
    
    	thisTokenSource := localTokenSource{
    		ctx:        ctx,
    		bucketName: bucketName,
    		brokerURL:  "yourURL.com/internal/broker",
    	}
    
    	// Wrap the TokenSource in an oauth2.ReuseTokenSource to enable automatic refreshing.
    	refreshableTS := oauth2.ReuseTokenSource(nil, thisTokenSource)
    	// You can now use the token source to access Google Cloud Storage resources as follows.
    	storageClient, err := storage.NewClient(ctx, option.WithTokenSource(refreshableTS))
    	if err != nil {
    		return fmt.Errorf("failed to create the storage client: %w", err)
    	}
    	defer storageClient.Close()
    	bkt := storageClient.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName)
    	obj := bkt.[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(objectName)
    	rc, err := obj.[NewReader](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewReader)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to retrieve the object: %w", err)
    	}
    	defer rc.Close()
    	data, err := io.ReadAll(rc)
    	if err != nil {
    		return fmt.Errorf("could not read the object's contents: %w", err)
    	}
    	// Data now contains the contents of the requested object.
    	output.[Write](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer_Write)(data)
    	return nil
    }
    

### Java

For Java, you can exchange and refresh tokens automatically with version 1.1.0 or later of the [`com.google.auth:google-auth-library-oauth2-http` artifact](https://search.maven.org/artifact/com.google.auth/google-auth-library-oauth2-http).

To check your artifact version, run the following Maven command in your application directory:
    
    
    mvn dependency:list -DincludeArtifactIds=google-auth-library-oauth2-http
    

The following example shows how a token broker can generate downscoped tokens:
    
    
    public static AccessToken getTokenFromBroker(String bucketName, String objectPrefix)
        throws IOException {
      // Retrieve the source credentials from ADC.
      GoogleCredentials sourceCredentials =
          GoogleCredentials.getApplicationDefault()
              .createScoped("https://www.googleapis.com/auth/cloud-platform");
    
      // Initialize the Credential Access Boundary rules.
      String availableResource = "//storage.googleapis.com/projects/_/buckets/" + bucketName;
    
      // Downscoped credentials will have readonly access to the resource.
      String availablePermission = "inRole:roles/storage.objectViewer";
    
      // Only objects starting with the specified prefix string in the object name will be allowed
      // read access.
      String expression =
          "resource.name.startsWith('projects/_/buckets/"
              + bucketName
              + "/objects/"
              + objectPrefix
              + "')";
    
      // Build the AvailabilityCondition.
      CredentialAccessBoundary.AccessBoundaryRule.AvailabilityCondition availabilityCondition =
          CredentialAccessBoundary.AccessBoundaryRule.AvailabilityCondition.newBuilder()
              .setExpression(expression)
              .build();
    
      // Define the single access boundary rule using the above properties.
      CredentialAccessBoundary.AccessBoundaryRule rule =
          CredentialAccessBoundary.AccessBoundaryRule.newBuilder()
              .setAvailableResource(availableResource)
              .addAvailablePermission(availablePermission)
              .setAvailabilityCondition(availabilityCondition)
              .build();
    
      // Define the Credential Access Boundary with all the relevant rules.
      CredentialAccessBoundary credentialAccessBoundary =
          CredentialAccessBoundary.newBuilder().addRule(rule).build();
    
      // Create the downscoped credentials.
      DownscopedCredentials downscopedCredentials =
          DownscopedCredentials.newBuilder()
              .setSourceCredential(sourceCredentials)
              .setCredentialAccessBoundary(credentialAccessBoundary)
              .build();
    
      // Retrieve the token.
      // This will need to be passed to the Token Consumer.
      AccessToken accessToken = downscopedCredentials.refreshAccessToken();
      return accessToken;
    }

The following example shows how a token consumer can use a refresh handler to automatically obtain and refresh downscoped tokens:
    
    
    public static void tokenConsumer(final String bucketName, final String objectName)
        throws IOException {
      // You can pass an `OAuth2RefreshHandler` to `OAuth2CredentialsWithRefresh` which will allow the
      // library to seamlessly handle downscoped token refreshes on expiration.
      OAuth2CredentialsWithRefresh.OAuth2RefreshHandler handler =
          new OAuth2CredentialsWithRefresh.OAuth2RefreshHandler() {
            @Override
            public AccessToken refreshAccessToken() throws IOException {
              // The common pattern of usage is to have a token broker pass the downscoped short-lived
              // access tokens to a token consumer via some secure authenticated channel.
              // For illustration purposes, we are generating the downscoped token locally.
              // We want to test the ability to limit access to objects with a certain prefix string
              // in the resource bucket. objectName.substring(0, 3) is the prefix here. This field is
              // not required if access to all bucket resources are allowed. If access to limited
              // resources in the bucket is needed, this mechanism can be used.
              return getTokenFromBroker(bucketName, objectName.substring(0, 3));
            }
          };
    
      // Downscoped token retrieved from token broker.
      AccessToken downscopedToken = handler.refreshAccessToken();
    
      // Create the OAuth2CredentialsWithRefresh from the downscoped token and pass a refresh handler
      // which will handle token expiration.
      // This will allow the consumer to seamlessly obtain new downscoped tokens on demand every time
      // token expires.
      OAuth2CredentialsWithRefresh credentials =
          OAuth2CredentialsWithRefresh.newBuilder()
              .setAccessToken(downscopedToken)
              .setRefreshHandler(handler)
              .build();
    
      // Use the credentials with the Cloud Storage SDK.
      StorageOptions options = StorageOptions.newBuilder().setCredentials(credentials).build();
      Storage storage = options.getService();
    
      // Call Cloud Storage APIs.
      Blob blob = storage.get(bucketName, objectName);
      String content = new String(blob.getContent());
      System.out.println(
          "Retrieved object, "
              + objectName
              + ", from bucket,"
              + bucketName
              + ", with content: "
              + content);
    }

### Node.js

For Node.js, you can exchange and refresh tokens automatically with version 7.9.0 or later of the [`google-auth-library` package](https://github.com/googleapis/google-auth-library-nodejs).

To check your package version, run the following command in your application directory:
    
    
    npm list google-auth-library
    

The following example shows how a token broker can generate downscoped tokens:
    
    
    // Imports the Google Auth libraries.
    const {GoogleAuth, DownscopedClient} = require('[google-auth-library](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/overview.html)');
    /**
     * Simulates token broker generating downscoped tokens for specified bucket.
     *
     * @param bucketName The name of the Cloud Storage bucket.
     * @param objectPrefix The prefix string of the object name. This is used
     *        to ensure access is restricted to only objects starting with this
     *        prefix string.
     */
    async function getTokenFromBroker(bucketName, objectPrefix) {
      const googleAuth = new [GoogleAuth](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/google-auth-library/googleauth.html)({
        scopes: 'https://www.googleapis.com/auth/cloud-platform',
      });
    
      // Define the Credential Access Boundary object.
      const cab = {
        // Define the access boundary.
        accessBoundary: {
          // Define the single access boundary rule.
          accessBoundaryRules: [
            {
              availableResource: `//storage.googleapis.com/projects/_/buckets/${bucketName}`,
              // Downscoped credentials will have readonly access to the resource.
              availablePermissions: ['inRole:roles/storage.objectViewer'],
              // Only objects starting with the specified prefix string in the object name
              // will be allowed read access.
              availabilityCondition: {
                expression:
                  "resource.name.startsWith('projects/_/buckets/" +
                  `${bucketName}/objects/${objectPrefix}')`,
              },
            },
          ],
        },
      };
    
      // Obtain an authenticated client via ADC.
      const client = await googleAuth.[getClient](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/google-auth-library/googleauth.html)();
    
      // Use the client to create a DownscopedClient.
      const cabClient = new [DownscopedClient](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/google-auth-library/downscopedclient.html)(client, cab);
    
      // Refresh the tokens.
      const refreshedAccessToken = await cabClient.getAccessToken();
    
      // This will need to be passed to the token consumer.
      return refreshedAccessToken;
    }

The following example shows how a token consumer can provide a refresh handler that automatically obtains and refreshes downscoped tokens:
    
    
    // Imports the Google Auth and Google Cloud libraries.
    const {OAuth2Client} = require('[google-auth-library](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/overview.html)');
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    /**
     * Simulates token consumer generating calling GCS APIs using generated
     * downscoped tokens for specified bucket.
     *
     * @param bucketName The name of the Cloud Storage bucket.
     * @param objectName The name of the object in the Cloud Storage bucket
     *        to read.
     */
    async function tokenConsumer(bucketName, objectName) {
      // Create the OAuth credentials (the consumer).
      const oauth2Client = new [OAuth2Client](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/google-auth-library/oauth2client.html)();
      // We are defining a refresh handler instead of a one-time access
      // token/expiry pair.
      // This will allow the consumer to obtain new downscoped tokens on
      // demand every time a token is expired, without any additional code
      // changes.
      oauth2Client.[refreshHandler](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/google-auth-library/oauth2client.html) = async () => {
        // The common pattern of usage is to have a token broker pass the
        // downscoped short-lived access tokens to a token consumer via some
        // secure authenticated channel. For illustration purposes, we are
        // generating the downscoped token locally. We want to test the ability
        // to limit access to objects with a certain prefix string in the
        // resource bucket. objectName.substring(0, 3) is the prefix here. This
        // field is not required if access to all bucket resources are allowed.
        // If access to limited resources in the bucket is needed, this mechanism
        // can be used.
        const refreshedAccessToken = await getTokenFromBroker(
          bucketName,
          objectName.substring(0, 3)
        );
        return {
          access_token: refreshedAccessToken.token,
          expiry_date: refreshedAccessToken.expirationTime,
        };
      };
    
      const storageOptions = {
        projectId: process.env.GOOGLE_CLOUD_PROJECT,
        authClient: oauth2Client,
      };
    
      const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)(storageOptions);
      const downloadFile = await storage
        .bucket(bucketName)
        .file(objectName)
        .[download](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/file_2.html)();
      console.log(downloadFile.toString('utf8'));
    }

### Python

For Python, you can exchange and refresh tokens automatically with version 2.0.0 or later of the [`google-auth` package](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-auth).

To check your package version, run the following command in the environment where the package is installed:
    
    
    pip show google-auth
    

The following example shows how a token broker can generate downscoped tokens:
    
    
    import google.auth
    
    from google.auth import downscoped
    from google.auth.transport import requests
    
    def get_token_from_broker(bucket_name, object_prefix):
        """Simulates token broker generating downscoped tokens for specified bucket.
    
        Args:
            bucket_name (str): The name of the Cloud Storage bucket.
            object_prefix (str): The prefix string of the object name. This is used
                to ensure access is restricted to only objects starting with this
                prefix string.
    
        Returns:
            Tuple[str, datetime.datetime]: The downscoped access token and its expiry date.
        """
        # Initialize the Credential Access Boundary rules.
        available_resource = f"//storage.googleapis.com/projects/_/buckets/{bucket_name}"
        # Downscoped credentials will have readonly access to the resource.
        available_permissions = ["inRole:roles/storage.objectViewer"]
        # Only objects starting with the specified prefix string in the object name
        # will be allowed read access.
        availability_expression = (
            "resource.name.startsWith('projects/_/buckets/{}/objects/{}')".format(
                bucket_name, object_prefix
            )
        )
        availability_condition = downscoped.AvailabilityCondition(availability_expression)
        # Define the single access boundary rule using the above properties.
        rule = downscoped.AccessBoundaryRule(
            available_resource=available_resource,
            available_permissions=available_permissions,
            availability_condition=availability_condition,
        )
        # Define the Credential Access Boundary with all the relevant rules.
        credential_access_boundary = downscoped.CredentialAccessBoundary(rules=[rule])
    
        # Retrieve the source credentials via ADC.
        source_credentials, _ = google.auth.default()
        if source_credentials.requires_scopes:
            source_credentials = source_credentials.with_scopes(
                ["https://www.googleapis.com/auth/cloud-platform"]
            )
    
        # Create the downscoped credentials.
        downscoped_credentials = downscoped.Credentials(
            source_credentials=source_credentials,
            credential_access_boundary=credential_access_boundary,
        )
    
        # Refresh the tokens.
        downscoped_credentials.refresh(requests.Request())
    
        # These values will need to be passed to the token consumer.
        access_token = downscoped_credentials.token
        expiry = downscoped_credentials.expiry
        return (access_token, expiry)
    
    

The following example shows how a token consumer can provide a refresh handler that automatically obtains and refreshes downscoped tokens:
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    from google.oauth2 import credentials
    
    def token_consumer(bucket_name, object_name):
        """Tests token consumer readonly access to the specified object.
    
        Args:
            bucket_name (str): The name of the Cloud Storage bucket.
            object_name (str): The name of the object in the Cloud Storage bucket
                to read.
        """
    
        # Create the OAuth credentials from the downscoped token and pass a
        # refresh handler to handle token expiration. We are passing a
        # refresh_handler instead of a one-time access token/expiry pair.
        # This will allow the consumer to obtain new downscoped tokens on
        # demand every time a token is expired, without any additional code
        # changes.
        def refresh_handler(request, scopes=None):
            # The common pattern of usage is to have a token broker pass the
            # downscoped short-lived access tokens to a token consumer via some
            # secure authenticated channel.
            # For illustration purposes, we are generating the downscoped token
            # locally.
            # We want to test the ability to limit access to objects with a certain
            # prefix string in the resource bucket. object_name[0:3] is the prefix
            # here. This field is not required if access to all bucket resources are
            # allowed. If access to limited resources in the bucket is needed, this
            # mechanism can be used.
            return get_token_from_broker(bucket_name, object_prefix=object_name[0:3])
    
        creds = credentials.Credentials(
            None,
            scopes=["https://www.googleapis.com/auth/cloud-platform"],
            refresh_handler=refresh_handler,
        )
    
        # Initialize a Cloud Storage client with the oauth2 credentials.
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)(credentials=creds)
        # The token broker has readonly access to the specified bucket object.
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        blob = bucket.blob(object_name)
        print(blob.[download_as_bytes](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_bytes)().decode("utf-8"))
    
    

#### Exchange and refresh the access token manually

A token broker can use the Security Token Service API to exchange an access token for a downscoped access token. It can then provide the downscoped token to a token consumer.

To exchange the access token, use the following HTTP method and URL:
    
    
    POST https://sts.googleapis.com/v1/token
    

Set the `Content-Type` header in the request to `application/x-www-form-urlencoded`. Include the following fields in the request body:

Fields  
---  
`grant_type` |  `string` Use the value `urn:ietf:params:oauth:grant-type:token-exchange`.   
`options` |  `string` A JSON-formatted Credential Access Boundary, encoded with [percent encoding](https://developer.mozilla.org/en-US/docs/Glossary/percent-encoding).   
`requested_token_type` |  `string` Use the value `urn:ietf:params:oauth:token-type:access_token`.   
`subject_token` |  `string` The OAuth 2.0 access token that you want to exchange.   
`subject_token_type` |  `string` Use the value `urn:ietf:params:oauth:token-type:access_token`.   
  
The response is a JSON object that contains the following fields:

Fields  
---  
`access_token` |  `string` A downscoped OAuth 2.0 access token that respects the Credential Access Boundary.   
`expires_in` |  `number` The amount of time until the downscoped token expires, in seconds.  This field is included only if the original access token represents a service account. When this field is not included, the downscoped token has the same time to expire as the original access token.   
`issued_token_type` |  `string` Contains the value `urn:ietf:params:oauth:token-type:access_token`.   
`token_type` |  `string` Contains the value `Bearer`.   
  
For example, if a JSON-formatted Credential Access Boundary is stored in the file `./access-boundary.json`, you can use the following [`curl`](https://curl.haxx.se/) command to exchange the access token. Replace `original-token` with the original access token:
    
    
    curl -H "Content-Type:application/x-www-form-urlencoded" \
        -X POST \
        https://sts.googleapis.com/v1/token \
        -d "grant_type=urn:ietf:params:oauth:grant-type:token-exchange&subject_token_type=urn:ietf:params:oauth:token-type:access_token&requested_token_type=urn:ietf:params:oauth:token-type:access_token&subject_token=original-token" \
        --data-urlencode "options=$(cat ./access-boundary.json)"

The response is similar to the following example:
    
    
    {
      "access_token": "ya29.dr.AbCDeFg-123456...",
      "issued_token_type": "urn:ietf:params:oauth:token-type:access_token",
      "token_type": "Bearer",
      "expires_in": 3600
    }
    

When a token consumer requests a downscoped token, the token broker responds with both the downscoped token and the number of seconds until it expires. If the token has expired, the server rejects the request. To refresh the downscoped token, the consumer can request a downscoped token from the broker before the existing token expires.

## What's next

  * Learn about [access control for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control).
  * Create a [short-lived service account credential](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials).
  * Create an OAuth 2.0 access token for a service account with one of the following methods: 
    * [Server-to-server OAuth 2.0 flow](https://developers.google.com/identity/protocols/OAuth2ServiceAccount)
    * [Service Account Credentials API](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials#sa-credentials-oauth)
  * Create an OAuth 2.0 access token [for a user](https://developers.google.com/identity/protocols/OAuth2WebServer#obtainingaccesstokens).
  * See the [permissions in each predefined role](https://docs.cloud.google.com/iam/docs/roles-permissions).
  * Learn about [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
