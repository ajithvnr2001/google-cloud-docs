---
url: https://docs.cloud.google.com/run/docs/authenticating/service-to-service/
title: Authenticating service-to-service \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:29.329187+00:00
---

# Authenticating service-to-service  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/authenticating/service-to-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Authenticating service-to-service Stay organized with collections  Save and categorize content based on your preferences. 

If your architecture is using multiple services, these services likely need to communicate with each other, using either asynchronous or synchronous means. Many of these services may be private and therefore [require credentials for access](https://docs.cloud.google.com/run/docs/securing/managing-access).

**Note:** There are no networking charges for service-to-service traffic between two services in the same region.

For _asynchronous_ communication, you can use the following Google Cloud services:

  * [Cloud Tasks](https://docs.cloud.google.com/run/docs/triggering/using-tasks) for one to one asynchronous communication
  * [Pub/Sub](https://docs.cloud.google.com/run/docs/events/pubsub-push) for one to many, one to one, and many to one asynchronous communication
  * [Cloud Scheduler](https://docs.cloud.google.com/run/docs/triggering/using-scheduler) for regularly scheduled asynchronous communication
  * [Eventarc](https://docs.cloud.google.com/eventarc/docs/creating-triggers) for event-based communication



In all of these cases, the service used manages the interaction with the receiving service, based on the configuration you set up.

But for _synchronous_ communication, your service calls another service directly, over HTTP, using its endpoint URL. For this use case, you should make sure that each service is only able to make requests to specific services. For example, if you have a `login` service, it should be able to access the `user-profiles` service, but not the `search` service.

In this situation, Google recommends that you use [IAM](https://docs.cloud.google.com/iam/docs/understanding-service-accounts) and a service identity based on a [per-service user-managed service account](https://docs.cloud.google.com/run/docs/securing/service-identity#per-service-identity) that has been granted the [minimum set](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#limit-service-account-privileges) of permissions required to do its work.

In addition, the request must present proof of the calling service's identity. To do this, configure your calling service to add a Google-signed [OpenID Connect](https://openid.net/connect/) ID token as part of the request.

## Set up the service account

**Note:** If you do not have a service account you want to use, you can [create a new one](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating).

To set up a service account, you configure the receiving service to accept requests from the calling service by making the calling service's service account a _principal_ on the receiving service. Then you grant that service account the Cloud Run Invoker (`roles/run.invoker`) role. To do both of these tasks, follow the instructions in the appropriate tab:

### Console UI

  1. Go to the Google Cloud console: 

[Go to Google Cloud console](https://console.cloud.google.com/run/)

  2. Select the receiving service.

  3. Click **Show Info Panel** in the top right corner to show the **Permissions** tab.

  4. Click **Add principal**.

     1. Enter the identity of the calling service. This is usually an email address, by default `PROJECT_NUMBER-compute@developer.gserviceaccount.com`.

     2. Select the `Cloud Run Invoker` role from the **Select a role** drop-down menu.

     3. Click **Save**.




###  gcloud 

Use the `gcloud run services add-iam-policy-binding` command:
    
    
    gcloud run services add-iam-policy-binding RECEIVING_SERVICE \
      --member='serviceAccount:CALLING_SERVICE_IDENTITY' \
      --role='roles/run.invoker'

where `RECEIVING_SERVICE` is the name of the receiving service, and `CALLING_SERVICE_IDENTITY` is the email address of the service account, by default `PROJECT_NUMBER-compute@developer.gserviceaccount.com`.

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_service" "public" {
      name     = "public-service"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
          # TODO<developer>: replace this with a public service container
          # (This service can be invoked by anyone on the internet)
          image = "us-docker.pkg.dev/cloudrun/container/hello"
    
          # Include a reference to the private Cloud Run
          # service's URL as an environment variable.
          env {
            name  = "URL"
            value = google_cloud_run_v2_service.private.uri
          }
        }
        # Give the "public" Cloud Run service
        # a service account's identity
        service_account = google_service_account.default.email
      }
    }

Replace `us-docker.pkg.dev/cloudrun/container/hello` with a reference to your container image.

The following Terraform code makes the initial service public.
    
    
    data "google_iam_policy" "public" {
      binding {
        role = "roles/run.invoker"
        members = [
          "allUsers",
        ]
      }
    }
    
    resource "google_cloud_run_service_iam_policy" "public" {
      location = google_cloud_run_v2_service.public.location
      project  = google_cloud_run_v2_service.public.project
      service  = google_cloud_run_v2_service.public.name
    
      policy_data = data.google_iam_policy.public.policy_data
    }

The following Terraform code creates a second Cloud Run service intended to be _private_.
    
    
    resource "google_cloud_run_v2_service" "private" {
      name     = "private-service"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
          // TODO<developer>: replace this with a private service container
          // (This service should only be invocable by the public service)
          image = "us-docker.pkg.dev/cloudrun/container/hello"
        }
      }
    }

Replace `us-docker.pkg.dev/cloudrun/container/hello` with a reference to your container image.

The following Terraform code creates a service account.
    
    
    resource "google_service_account" "default" {
      account_id   = "cloud-run-interservice-id"
      description  = "Identity used by a public Cloud Run service to call private Cloud Run services."
      display_name = "cloud-run-interservice-id"
    }

The following Terraform code makes the second service private by granting only the calling service account permission to invoke it.
    
    
    data "google_iam_policy" "private" {
      binding {
        role = "roles/run.invoker"
        members = [
          "serviceAccount:${google_service_account.default.email}",
        ]
      }
    }
    
    resource "google_cloud_run_service_iam_policy" "private" {
      location = google_cloud_run_v2_service.private.location
      project  = google_cloud_run_v2_service.private.project
      service  = google_cloud_run_v2_service.private.name
    
      policy_data = data.google_iam_policy.private.policy_data
    }

## Acquire and configure the ID token

After you grant the proper role to the calling service account, follow these steps:

  1. Fetch a Google-signed [ID token](https://docs.cloud.google.com/docs/authentication/token-types#identity-tokens) by using one of the methods described in the following section. Set the audience claim (`aud`) to the URL of the receiving service or a configured [custom audience](https://docs.cloud.google.com/run/docs/configuring/custom-audiences). If you are not using a custom audience, the `aud` value must remain as the URL of the service, even when making requests to a [specific traffic tag](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration#tags).

**Note:** Custom domains are currently not supported for the `aud` value. 
  2. Add the ID token you fetched from the previous step into one of the following headers in the request to the receiving service:

     * An `Authorization: Bearer ID_TOKEN` header.
     * An `X-Serverless-Authorization: Bearer ID_TOKEN` header. You can use this header if your application already uses the `Authorization` header for custom authorization. This removes the signature before passing the token to the user container.
**Note:** If you provide both headers, only the `X-Serverless-Authorization` header is checked.



For other ways to get an ID token that are not described on this page, see [Methods for getting an ID token](https://docs.cloud.google.com/docs/authentication/get-id-token#methods).

### Use the authentication libraries

One way to acquire and configure the ID token process is to use the authentication libraries. This code works in **any environment** , even outside of Google Cloud, where the libraries can obtain authentication credentials for a service account. To use this method, you [download a service account key file](https://docs.cloud.google.com/iam/docs/keys-create-delete#creating), and set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of the service account key file. For more information, see [service account key](https://docs.cloud.google.com/docs/authentication/set-up-adc-on-premises#wlif-key).

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

This code does not accept authentication credentials for a [user account](https://docs.cloud.google.com/docs/authentication#user-accounts).

###  Node.js 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // Example: https://my-cloud-run-service.run.app/books/delete/12345
    // const url = 'https://TARGET_HOSTNAME/TARGET_URL';
    
    // Example (Cloud Run): https://my-cloud-run-service.run.app/
    // const targetAudience = 'https://TARGET_AUDIENCE/';
    
    const {GoogleAuth} = require('[google-auth-library](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/overview.html)');
    const auth = new [GoogleAuth](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/google-auth-library/googleauth.html)();
    
    async function request() {
      console.info(`request ${url} with target audience ${targetAudience}`);
      const client = await [auth](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/overview.html).[getIdTokenClient](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/google-auth-library/googleauth.html)(targetAudience);
    
      // Alternatively, one can use `client.idTokenProvider.fetchIdToken`
      // to return the ID Token.
      const res = await client.fetch(url);
      console.info(res.data);
    }
    
    request().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

###  Python 
    
    
    import urllib
    
    import google.auth.transport.requests
    import google.oauth2.id_token
    
    
    def make_authorized_get_request(endpoint, audience):
        """
        make_authorized_get_request makes a GET request to the specified HTTP endpoint
        by authenticating with the ID token obtained from the google-auth client library
        using the specified audience value.
        """
    
        # Cloud Run uses your service's hostname as the `audience` value
        # audience = 'https://my-cloud-run-service.run.app/'
        # For Cloud Run, `endpoint` is the URL (hostname + path) receiving the request
        # endpoint = 'https://my-cloud-run-service.run.app/my/awesome/url'
    
        req = urllib.request.Request(endpoint)
    
        auth_req = google.auth.transport.requests.Request()
        id_token = google.oauth2.id_token.fetch_id_token(auth_req, audience)
    
        req.add_header("Authorization", f"Bearer {id_token}")
        response = urllib.request.urlopen(req)
    
        return response.read()
    
    

###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"google.golang.org/api/idtoken"
    )
    
    // `makeGetRequest` makes a request to the provided `targetURL`
    // with an authenticated client using audience `audience`.
    func makeGetRequest(w io.Writer, targetURL string, audience string) error {
    	// Example `audience` value (Cloud Run): https://my-cloud-run-service.run.app/
    	// (`targetURL` and `audience` will differ for non-root URLs and GET parameters)
    	ctx := context.Background()
    
    	// client is a http.Client that automatically adds an "Authorization" header
    	// to any requests made.
    	client, err := idtoken.NewClient(ctx, audience)
    	if err != nil {
    		return fmt.Errorf("idtoken.NewClient: %w", err)
    	}
    
    	resp, err := client.Get(targetURL)
    	if err != nil {
    		return fmt.Errorf("client.Get: %w", err)
    	}
    	defer resp.Body.Close()
    	if _, err := io.Copy(w, resp.Body); err != nil {
    		return fmt.Errorf("io.Copy: %w", err)
    	}
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.api.client.http.[GenericUrl](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.GenericUrl.html);
    import com.google.api.client.http.[HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html);
    import com.google.api.client.http.[HttpResponse](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponse.html);
    import com.google.api.client.http.[HttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import com.google.auth.oauth2.[IdTokenCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.html);
    import com.google.auth.oauth2.[IdTokenProvider](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.html);
    import java.io.IOException;
    
    public class Authentication {
    
      // makeGetRequest makes a GET request to the specified Cloud Run or
      // Cloud Functions endpoint `serviceUrl` (must be a complete URL), by
      // authenticating with an ID token retrieved from Application Default
      // Credentials using the specified `audience`.
      //
      // Example `audience` value (Cloud Run): https://my-cloud-run-service.run.app/
      public static [HttpResponse](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponse.html) makeGetRequest(String serviceUrl, String audience) throws IOException {
        [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html) credentials = [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html).[getApplicationDefault](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html#com_google_auth_oauth2_GoogleCredentials_getApplicationDefault__)();
        if (!(credentials instanceof [IdTokenProvider](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.html))) {
          throw new IllegalArgumentException("Credentials are not an instance of IdTokenProvider.");
        }
        [IdTokenCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.html) tokenCredential =
            [IdTokenCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.html).newBuilder()
                .[setIdTokenProvider](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.Builder.html#com_google_auth_oauth2_IdTokenCredentials_Builder_setIdTokenProvider_com_google_auth_oauth2_IdTokenProvider_)(([IdTokenProvider](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.html)) credentials)
                .[setTargetAudience](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.Builder.html#com_google_auth_oauth2_IdTokenCredentials_Builder_setTargetAudience__org_jspecify_annotations_Nullable_java_lang_String_)(audience)
                .build();
    
        [GenericUrl](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.GenericUrl.html) genericUrl = new [GenericUrl](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.GenericUrl.html)(serviceUrl);
        [HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html) adapter = new [HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html)(tokenCredential);
        [HttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport.html) transport = new [NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html)();
        [HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html) request = transport.[createRequestFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport.html#com_google_api_client_http_HttpTransport_createRequestFactory__)(adapter).[buildGetRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestFactory.html#com_google_api_client_http_HttpRequestFactory_buildGetRequest_com_google_api_client_http_GenericUrl_)(genericUrl);
        return request.[execute](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html#com_google_api_client_http_HttpRequest_execute__)();
      }
    }

### Use the metadata server

If for some reason you **cannot** use the authentication libraries, you can fetch an ID token from the [Compute metadata server](https://docs.cloud.google.com/run/docs/securing/service-identity#identity_tokens) while your container is running on Cloud Run. Note that this method does not work outside of Google Cloud, including from your local machine.
    
    
    curl "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/identity?audience=[AUDIENCE]" \
         -H "Metadata-Flavor: Google"
    

Where AUDIENCE is the URL of the service you are invoking or a configured [custom audience](https://docs.cloud.google.com/run/docs/configuring/custom-audiences).

The following table summarizes the main parts of a metadata query request:

Components | Description  
---|---  
Root URL | All metadata values are defined as sub-paths below the following root URL:
    
    
    http://metadata.google.internal/computeMetadata/v1  
  
Request header | The following header must be in each request:
    
    
    Metadata-Flavor: Google

This header indicates that the request was sent with the intention of retrieving metadata values, rather than unintentionally from an insecure source, and lets the metadata server return the data you requested. If you don't provide this header, the metadata server denies your request.  **Note:** Previously, the `X-Google-Metadata-Request: True` header was required in requests. Both of these headers are still supported, but we recommend that you use the `Metadata-Flavor` header rather than the `X-Google-Metadata-Request: True` header.  
**Note:** ID tokens are [JSON Web Tokens (JWTs)](https://en.wikipedia.org/wiki/JSON_Web_Token) that expire approximately an hour after creation. If you fetch tokens from the [metadata server](https://docs.cloud.google.com/run/docs/securing/service-identity#identity_tokens), you will always get a valid token. If you choose to cache tokens yourself, you can decode the token and check the `exp` time to see if you need to refresh the token.

For an end-to-end walkthrough of an application using this service-to-service authentication technique, follow the [securing Cloud Run services tutorial](https://docs.cloud.google.com/run/docs/tutorials/secure-services).

### Use workload identity federation from outside Google Cloud

If your environment uses an identity provider supported by [workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation), you can use the following method to securely authenticate to your Cloud Run service from outside Google Cloud:

  1. Set up your service account as described in Set up the service account on this page.

  2. Configure workload identity federation for your identity provider as described in [Configuring workload identity federation](https://docs.cloud.google.com/iam/docs/configuring-workload-identity-federation).

  3. Follow the instructions in [Granting external identities permission to impersonate a service account](https://docs.cloud.google.com/iam/docs/using-workload-identity-federation#impersonate).

  4. [Use the REST API to acquire a short-lived token](https://docs.cloud.google.com/iam/docs/using-workload-identity-federation#rest), but instead of calling [`generateAccessToken`](https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/generateAccessToken) to obtain an access token, call [`generateIdToken`](https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/generateIdToken) instead to get an ID token.

For example, using cURL:
         
         ID_TOKEN=$(curl -0 -X POST https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/SERVICE_ACCOUNT:generateIdToken \
           -H "Content-Type: text/json; charset=utf-8" \
           -H "Authorization: Bearer $STS_TOKEN" \
           -d @- <<EOF | jq -r .token
           {
               "audience": "SERVICE_URL"
           }
         EOF
         )
         echo $ID_TOKEN

Where `SERVICE_ACCOUNT` is the email address of the service account the workload identity pool is configured to access, and `SERVICE_URL` is the URL of the Cloud Run service you are invoking. This value should remain as the URL of the service, even when making requests to a [specific traffic tag](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration#tags). `$STS_TOKEN` is the Security Token Service token you received in the previous step in the Workload Identity Federation instructions.




You can include the ID token from the previous step in the request to the service by using an `Authorization: Bearer ID_TOKEN` header or an `X-Serverless-Authorization: Bearer ID_TOKEN` header. If both headers are provided, only the `X-Serverless-Authorization` header is checked.

### Use a downloaded service account key from outside Google Cloud

If Workload Identity Federation is not appropriate for your environment, you can use a downloaded service account key to authenticate from outside Google Cloud. Update your client code to use the authentication libraries as described previously. For more information, see [service account key](https://docs.cloud.google.com/docs/authentication/set-up-adc-on-premises#wlif-key).

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

You can acquire a Google-signed ID token by using a self-signed JWT, but this is quite complicated and potentially error-prone. The basic steps are as follows:

  1. Self-sign a service account JWT with the `target_audience` claim set to the URL of the receiving service or a configured [custom audience](https://docs.cloud.google.com/run/docs/configuring/custom-audiences). If not using custom domains, the `target_audience` value should remain as the URL of the service, even when making requests to a [specific traffic tag](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration#tags).

  2. Exchange the self-signed JWT for a Google-signed ID token, which should have the `aud` claim set to the preceding URL.

  3. Include the ID token in the request to the service by using an `Authorization: Bearer ID_TOKEN` header or an `X-Serverless-Authorization: Bearer ID_TOKEN` header. If both headers are provided, only the `X-Serverless-Authorization` header is checked.




## Receive authenticated requests

Within the receiving private service, you can parse the authorization header to receive the information being sent by the Bearer token.

###  Python 
    
    
    from flask import Request
    
    from google.auth.exceptions import GoogleAuthError
    from google.auth.transport import requests
    from google.oauth2 import id_token
    
    
    def receive_request_and_parse_auth_header(request: Request) -> str:
        """Parse the authorization header, validate the Bearer token
        and decode the token to get its information.
    
        Args:
            request: Flask request object.
    
        Returns:
            One of the following:
            a) The email from the request's Authorization header.
            b) A welcome message for anonymous users.
            c) An error description.
        """
        auth_header = request.headers.get("Authorization")
        if auth_header:
            # Split the auth type and value from the header.
            auth_type, creds = auth_header.split(" ", 1)
    
            if auth_type.lower() == "bearer":
                # Find more information about `verify_token` function here:
                # https://google-auth.readthedocs.io/en/master/reference/google.oauth2.id_token.html#google.oauth2.id_token.verify_token
                try:
                    decoded_token = id_token.verify_token(creds, requests.Request())
                    return f"Hello, {decoded_token['email']}!\n"
                except GoogleAuthError as e:
                    return f"Invalid token: {e}\n"
            else:
                return f"Unhandled header format ({auth_type}).\n"
    
        return "Hello, anonymous user.\n"

###  Java 
    
    
    import com.google.api.client.googleapis.auth.oauth2.[GoogleIdToken](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleIdToken.html);
    import com.google.api.client.googleapis.auth.oauth2.[GoogleIdTokenVerifier](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleIdTokenVerifier.html);
    import com.google.api.client.http.apache.v2.[ApacheHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.apache.v2.ApacheHttpTransport.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import java.util.Arrays;
    import java.util.Collection;
    import org.springframework.boot.SpringApplication;
    import org.springframework.boot.autoconfigure.SpringBootApplication;
    import org.springframework.http.HttpHeaders;
    import org.springframework.http.HttpStatus;
    import org.springframework.http.ResponseEntity;
    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.RequestHeader;
    import org.springframework.web.bind.annotation.RestController;
    
    @SpringBootApplication
    public class Authentication {
      @RestController
      class AuthenticationController {
    
        private final AuthenticationService authService = new AuthenticationService();
    
        @GetMapping("/")
        public ResponseEntity<String> getEmailFromAuthHeader(
            @RequestHeader(value = "Authorization", required = false) String authHeader) {
          String responseBody;
          if (authHeader == null) {
            responseBody = "Error verifying ID token: missing Authorization header";
            return new ResponseEntity<>(responseBody, HttpStatus.UNAUTHORIZED);
          }
    
          String email = authService.parseAuthHeader(authHeader);
          if (email == null) {
            responseBody = "Unauthorized request. Please supply a valid bearer token.";
            HttpHeaders headers = new HttpHeaders();
            headers.add("WWW-Authenticate", "Bearer");
            return new ResponseEntity<>(responseBody, headers, HttpStatus.UNAUTHORIZED);
          }
    
          responseBody = "Hello, " + email;
          return new ResponseEntity<>(responseBody, HttpStatus.OK);
        }
      }
    
      public class AuthenticationService {
        /*
         * Parse the authorization header, validate and decode the Bearer token.
         *
         * Args:
         *    authHeader: String of HTTP header with a Bearer token.
         *
         * Returns:
         *    A string containing the email from the token.
         *    null if the token is invalid or the email can't be retrieved.
         */
        public String parseAuthHeader(String authHeader) {
          // Split the auth type and value from the header.
          String[] authHeaderStrings = authHeader.split(" ");
          if (authHeaderStrings.length != 2) {
            System.out.println("Malformed Authorization header");
            return null;
          }
          String authType = authHeaderStrings[0];
          String tokenValue = authHeaderStrings[1];
          // Validate and decode the ID token in the header.
          if (!"bearer".equals(authType.toLowerCase())) {
            System.out.println("Unhandled header format: " + authType);
            return null;
          }
    
          // Get the service URL from the environment variable
          // set at the time of deployment.
          String serviceUrl = System.getenv("SERVICE_URL");
          // Define the expected audience as the Service Base URL.
          Collection<String> audience = Arrays.asList(serviceUrl);
    
          try {
            // Find more information about the verification process in:
            // https://developers.google.com/identity/sign-in/web/backend-auth#java
            // https://cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleIdTokenVerifier
            [GoogleIdTokenVerifier](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleIdTokenVerifier.html) verifier =
                new [GoogleIdTokenVerifier](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleIdTokenVerifier.html).Builder(new [ApacheHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.apache.v2.ApacheHttpTransport.html)(), new [GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html)())
                    .setAudience(audience)
                    .build();
            [GoogleIdToken](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleIdToken.html) googleIdToken = verifier.[verify](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleIdTokenVerifier.html#com_google_api_client_googleapis_auth_oauth2_GoogleIdTokenVerifier_verify_com_google_api_client_googleapis_auth_oauth2_GoogleIdToken_)(tokenValue);
    
            // More info about the structure for the decoded ID Token here:
            // https://cloud.google.com/docs/authentication/token-types#id
            // https://cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleIdToken
            // https://cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleIdToken.Payload
            [GoogleIdToken](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleIdToken.html).[Payload](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleIdToken.Payload.html) payload = googleIdToken.[getPayload](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleIdToken.html#com_google_api_client_googleapis_auth_oauth2_GoogleIdToken_getPayload__)();
            if (!payload.[getEmailVerified](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleIdToken.Payload.html#com_google_api_client_googleapis_auth_oauth2_GoogleIdToken_Payload_getEmailVerified__)()) {
              System.out.println("Invalid token. Email wasn't verified.");
              return null;
            }
            System.out.println("Email verified: " + payload.[getEmail](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleIdToken.Payload.html#com_google_api_client_googleapis_auth_oauth2_GoogleIdToken_Payload_getEmail__)());
            return payload.[getEmail](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.auth.oauth2.GoogleIdToken.Payload.html#com_google_api_client_googleapis_auth_oauth2_GoogleIdToken_Payload_getEmail__)();
    
          } catch (Exception exception) {
            System.out.println("Ivalid token: " + exception);
          }
          return null;
        }
      }
    
      public static void main(String[] args) {
        SpringApplication.run(Authentication.class, args);
      }
    

## What's next

  * Learn more about [ID token validation](https://developers.google.com/identity/openid-connect/openid-connect#validatinganidtoken)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
