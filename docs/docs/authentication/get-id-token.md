---
url: https://docs.cloud.google.com/docs/authentication/get-id-token/
title: Get an ID token \u00a0|\u00a0 Authentication \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:46.770395+00:00
---

# Get an ID token  |  Authentication  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/authentication/get-id-token/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Authentication ](https://docs.cloud.google.com/docs/authentication)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Get an ID token Stay organized with collections  Save and categorize content based on your preferences. 

This page describes some ways to acquire a Google-signed OpenID Connect (OIDC) ID token.

You need a Google-signed ID token for the following authentication use cases:

  * [ Accessing a Cloud Run service](https://docs.cloud.google.com/run/docs/authenticating/service-to-service)
  * [ Invoking a Cloud Run function](https://docs.cloud.google.com/functions/docs/securing/authenticating)
  * [Authenticating a user to an application secured by Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/authentication-howto)
  * [Making a request to an API deployed with API Gateway or Cloud Endpoints](https://docs.cloud.google.com/api-gateway/docs/authentication-method)



For information about ID token contents and lifetimes, see [ID tokens](https://docs.cloud.google.com/docs/authentication/token-types#identity-tokens).

ID tokens have a specific service or application that they can be used for, specified by the value of their `aud` claim. This document uses the term _target service_ to refer to the service or application that the ID token can be used to authenticate to.

When you get the ID token, you can include it in an `Authorization` header in the request to the target service.

## Methods for getting an ID token

There are various ways to get an ID token. This page describes the following methods:

  * Get an ID token from the metadata server
  * Use a connecting service to generate an ID token
  * Generate an ID token by impersonating a service account
  * Generate a generic ID token for development with Cloud Run and Cloud Run functions



If you need an ID token to be accepted by an application not hosted on Google Cloud, you can probably use these methods. However, you should determine what ID token claims the application requires.

### Get an ID token from the metadata server

When your code is running on a resource that can have a [service account attached to it](https://docs.cloud.google.com/iam/docs/attach-service-accounts#attaching-to-resources), the metadata server for the associated service can usually provide an ID token. The metadata server generates ID tokens for the attached service account. You cannot get an ID token based on user credentials from the metadata server.

You can get an ID token from the metadata server when your code is running on the following Google Cloud services:

  * [ Compute Engine](https://docs.cloud.google.com/compute/docs/instances/verifying-instance-identity#request_signature)
  * [ App Engine standard environment](https://docs.cloud.google.com/appengine/docs/standard/python3/runtime#metadata_server)
  * [ App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible/python/runtime#metadata_server)
  * [ Cloud Run functions](https://docs.cloud.google.com/functions/docs/securing/function-identity#metadata-server)
  * [Cloud Run](https://docs.cloud.google.com/run/docs/container-contract#metadata-server)
  * [ Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity#instance_metadata)
  * [ Cloud Build](https://docs.cloud.google.com/build/docs/securing-builds/authorize-service-to-service-access)



To retrieve an ID token from the metadata server, you query the identity endpoint for the service account, as shown in this example.

###  curl 

Replace `AUDIENCE` with the URI for the target service, for example `http://www.example.com`.
    
    
    curl -H "Metadata-Flavor: Google" \
      'http://metadata/computeMetadata/v1/instance/service-accounts/default/identity?audience=AUDIENCE'
    

###  PowerShell 

Replace `AUDIENCE` with the URI for the target service, for example `http://www.example.com`.
    
    
    $value = (Invoke-RestMethod `
      -Headers @{'Metadata-Flavor' = 'Google'} `
      -Uri "http://metadata/computeMetadata/v1/instance/service-accounts/default/identity?audience=AUDIENCE")
    $value
    

###  Java 

To run this code sample, you must install the [Auth Client Library for Java](https://github.com/googleapis/google-auth-library-java). 
    
    
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import com.google.auth.oauth2.[IdTokenCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.html);
    import com.google.auth.oauth2.[IdTokenProvider](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.html);
    import com.google.auth.oauth2.[IdTokenProvider](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.html).[Option](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.Option.html);
    import java.io.IOException;
    import java.security.GeneralSecurityException;
    import java.util.Arrays;
    
    public class IdTokenFromMetadataServer {
    
      public static void main(String[] args) throws IOException, GeneralSecurityException {
        // TODO(Developer): Replace the below variables before running the code.
    
        // The url or target audience to obtain the ID token for.
        String url = "https://example.com";
    
        getIdTokenFromMetadataServer(url);
      }
    
      // Use the Google Cloud metadata server to create an identity token and add it to the
      // HTTP request as part of an Authorization header.
      public static void getIdTokenFromMetadataServer(String url) throws IOException {
        // Construct the GoogleCredentials object which obtains the default configuration from your
        // working environment.
        [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html) googleCredentials = [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html).[getApplicationDefault](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html#com_google_auth_oauth2_GoogleCredentials_getApplicationDefault__)();
    
        [IdTokenCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.html) idTokenCredentials =
            [IdTokenCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.html).newBuilder()
                .[setIdTokenProvider](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.Builder.html#com_google_auth_oauth2_IdTokenCredentials_Builder_setIdTokenProvider_com_google_auth_oauth2_IdTokenProvider_)(([IdTokenProvider](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.html)) googleCredentials)
                .[setTargetAudience](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.Builder.html#com_google_auth_oauth2_IdTokenCredentials_Builder_setTargetAudience__org_jspecify_annotations_Nullable_java_lang_String_)(url)
                // Setting the ID token options.
                .[setOptions](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.Builder.html#com_google_auth_oauth2_IdTokenCredentials_Builder_setOptions__org_jspecify_annotations_Nullable_java_util_List_com_google_auth_oauth2_IdTokenProvider_Option__)(Arrays.asList([Option](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.Option.html).FORMAT_FULL, [Option](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.Option.html).LICENSES_TRUE))
                .build();
    
        // Get the ID token.
        // Once you've obtained the ID token, you can use it to make an authenticated call to the
        // target audience.
        String idToken = idTokenCredentials.[refreshAccessToken](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.html#com_google_auth_oauth2_IdTokenCredentials_refreshAccessToken__)().getTokenValue();
        System.out.println("Generated ID token.");
      }
    }

###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"golang.org/x/oauth2/google"
    	"google.golang.org/api/idtoken"
    	"google.golang.org/api/option"
    )
    
    // getIdTokenFromMetadataServer uses the Google Cloud metadata server environment
    // to create an identity token and add it to the HTTP request as part of an Authorization header.
    func getIdTokenFromMetadataServer(w io.Writer, url string) error {
    	// url := "http://www.example.com"
    
    	ctx := context.Background()
    
    	// Construct the GoogleCredentials object which obtains the default configuration from your
    	// working environment.
    	credentials, err := google.FindDefaultCredentials(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to generate default credentials: %w", err)
    	}
    
    	ts, err := idtoken.NewTokenSource(ctx, url, option.WithCredentials(credentials))
    	if err != nil {
    		return fmt.Errorf("failed to create NewTokenSource: %w", err)
    	}
    
    	// Get the ID token.
    	// Once you've obtained the ID token, you can use it to make an authenticated call
    	// to the target audience.
    	_, err = ts.Token()
    	if err != nil {
    		return fmt.Errorf("failed to receive token: %w", err)
    	}
    	fmt.Fprintf(w, "Generated ID token.\n")
    
    	return nil
    }
    

###  Node.js 

To run this code sample, you must install the [Google Auth Library for Node.js](https://github.com/googleapis/google-auth-library-nodejs)
    
    
    /**
     * TODO(developer):
     *  1. Uncomment and replace these variables before running the sample.
     */
    // const targetAudience = 'http://www.example.com';
    
    const {GoogleAuth} = require('[google-auth-library](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/overview.html)');
    
    async function getIdTokenFromMetadataServer() {
      const googleAuth = new [GoogleAuth](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/google-auth-library/googleauth.html)();
    
      const client = await googleAuth.[getIdTokenClient](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/google-auth-library/googleauth.html)(targetAudience);
    
      // Get the ID token.
      // Once you've obtained the ID token, you can use it to make an authenticated call
      // to the target audience.
      await client.[idTokenProvider](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/google-auth-library/idtokenclient.html).fetchIdToken(targetAudience);
      console.log('Generated ID token.');
    }
    
    getIdTokenFromMetadataServer();

###  Python 

To run this code sample, you must install the [Google Auth Python Library](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-auth). 
    
    
    import [google](https://docs.cloud.google.com/python/docs/reference/pubsub/latest)
    from google.auth import compute_engine
    import google.auth.transport.requests
    import google.oauth2.credentials
    
    
    def idtoken_from_metadata_server(url: str) -> None:
        """
        Use the Google Cloud metadata server in the Cloud Run (or AppEngine or Kubernetes etc.,)
        environment to create an identity token and add it to the HTTP request as part of an
        Authorization header.
    
        Args:
            url: The url or target audience to obtain the ID token for.
                Examples: http://www.example.com
        """
    
        request = [google](https://docs.cloud.google.com/python/docs/reference/pubsub/latest).auth.transport.[requests](https://docs.cloud.google.com/python/docs/reference/google-resumable-media/latest/google.resumable_media.requests.html).[Request](https://docs.cloud.google.com/python/docs/reference/policytroubleshooter-iam/latest/google.cloud.policytroubleshooter_iam_v3.types.ConditionContext.Request.html)()
        # Set the target audience.
        # Setting "use_metadata_identity_endpoint" to "True" will make the request use the default application
        # credentials. Optionally, you can also specify a specific service account to use by mentioning
        # the service_account_email.
        credentials = compute_engine.IDTokenCredentials(
            request=request, target_audience=url, use_metadata_identity_endpoint=True
        )
    
        # Get the ID token.
        # Once you've obtained the ID token, use it to make an authenticated call
        # to the target audience.
        credentials.refresh(request)
        # print(credentials.token)
        print("Generated ID token.")
    

###  Ruby 

To run this code sample, you must install the [Google Auth Library for Ruby](https://github.com/googleapis/google-auth-library-ruby). 
    
    
    require "googleauth"
    
    ##
    # Uses the Google Cloud metadata server environment to create an identity token
    # and add it to the HTTP request as part of an Authorization header.
    #
    # @param url [String] The url or target audience to obtain the ID token for
    #   (e.g. "http://www.example.com")
    #
    def auth_cloud_idtoken_metadata_server url:
      # Create the GCECredentials client.
      id_client = Google::Auth::[GCECredentials](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-GCECredentials.html).new target_audience: url
    
      # Get the ID token.
      # Once you've obtained the ID token, you can use it to make an authenticated call
      # to the target audience.
      id_client.[fetch_access_token](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-GCECredentials.html)
      puts "Generated ID token."
    
      id_client.refresh!
    end

### Use a connecting service to generate an ID token

Some Google Cloud services help you call other services. These connecting services might help determine when the call gets made, or manage a workflow that includes calling the service. The following services can automatically include an ID token, with the appropriate value for the `aud` claim, when they initiate a call to a service that requires an ID token:

Cloud Scheduler
     Cloud Scheduler is a fully managed enterprise-grade cron job scheduler. You can configure Cloud Scheduler to include either an ID token or an access token when it invokes another service. For more information, see [ Using authentication with HTTP Targets](https://docs.cloud.google.com/scheduler/docs/http-target-auth). 
Cloud Tasks
     Cloud Tasks lets you manage the execution of distributed tasks. You can configure a task to include either an ID token or an access token when it calls a service. For more information, see [ Using HTTP Target tasks with authentication tokens](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks#token). 
Pub/Sub
     Pub/Sub enables asynchronous communication between services. You can configure Pub/Sub to include an ID token with a message. For more information, see [ Authentication for push subscription](https://docs.cloud.google.com/pubsub/docs/push#authentication). 
Workflows
     Workflows is a fully managed orchestration platform that executes services in an order that you define: a _workflow_. You can define a workflow to include either an ID token or an access token when it invokes another service. For more information, see [ Make authenticated requests from a workflow](https://docs.cloud.google.com/workflows/docs/authenticate-from-workflow). 

### Generate an ID token by impersonating a service account

Service account impersonation allows a principal to generate short-lived credentials for a trusted service account. The principal can then use these credentials to authenticate as the service account.

Before a principal can impersonate a service account, it must have an IAM role on that service account that enables impersonation. If the principal is itself another service account, it might seem easier to simply provide the required permissions directly to that service account, and enable it to impersonate itself. This configuration, known as self-impersonation, creates a security vulnerability, because it lets the service account create an access token that can be refreshed in perpetuity.

Service account impersonation should always involve two principals: a principal that represents the caller, and the service account that is being impersonated, called the privilege-bearing service account.

To generate an ID token by impersonating a service account, you use the following general process.

For step-by-step instructions, see [Create an ID token](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct#sa-credentials-oidc).

  1. Identify or [create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create#creating) to be the privilege-bearing service account.

  2. Identify the required roles to invoke the target service. Grant these roles to the service account on the target service: 

     * For [ Cloud Run services](https://docs.cloud.google.com/run/docs/authenticating/service-to-service#set-up-sa), grant the Cloud Run Invoker role (`roles/run.invoker`). 
     * For [Cloud Run functions](https://docs.cloud.google.com/functions/docs/securing/authenticating), grant the Cloud Functions Invoker role (`roles/cloudfunctions.invoker`). 
     * For other target services, see the product documentation for the service. 
  3. Identify the principal that will perform the impersonation, and set up [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) to use the credentials for this principal.

For development environments, the principal is usually the user account you provided to ADC by using the gcloud CLI. However, if you're running on a resource with a service account attached, the attached service account is the principal.

  4. Grant the principal the Service Account OpenID Connect Identity Token Creator role (`roles/iam.serviceAccountOpenIdTokenCreator`).

  5. Use the [IAM Credentials API](https://docs.cloud.google.com/iam/docs/reference/credentials/rest) to generate the ID token for the authorized service account.

Replace the following:

     * AUDIENCE: The URI for the target service—for example, `http://www.example.com`.
     * SERVICE_ACCOUNT_EMAIL: The email address of the privilege-bearing service account.
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d '{"audience": "AUDIENCE", "includeEmail": "true"}' \
    https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/SERVICE_ACCOUNT_EMAIL:generateIdToken
    




### Generate a generic ID token for development with Cloud Run and Cloud Run functions

You can use the gcloud CLI to get an ID token for your user credentials that can be used with any Cloud Run service or Cloud Run function that the caller has the required IAM permissions to invoke. This token will not work for any other application.

**Warning:** be sure to keep these tokens secure, and never use them in a production environment. They are meant to be used during development only.

  * To generate a generic ID token, you use the [`gcloud auth print-identity-token` command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/print-identity-token):
        
        gcloud auth print-identity-token
        




## What's next

  * Understand [ID tokens](https://docs.cloud.google.com/docs/authentication/token-types#identity-tokens).
  * Use shell commands to [query the Compute Engine metadata server](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata).
  * Learn more about [authentication methods](https://docs.cloud.google.com/docs/authentication).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
