---
url: https://docs.cloud.google.com/functions/1stgendocs/securing/authenticating/
title: Authenticate for invocation (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:41.842756+00:00
---

# Authenticate for invocation (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/securing/authenticating/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Authenticate for invocation (1st gen)

To invoke an authenticated Cloud Run function, the underlying **principal** must meet the following requirements:

  * Have permission to invoke the function.
  * Provide an ID token when it invokes the function.



What is a principal? As described in [Secure your Cloud Run functions](https://docs.cloud.google.com/functions/1stgendocs/securing), Cloud Run functions supports two different kinds of identities, which are also called **principals** :

  * Service accounts: These are special accounts that serve as the identity of a non-person, like a function or an application or a VM. They give you a way to authenticate these non-persons.
  * User accounts: These accounts represent people, either as individual Google Account holders or as part of a Google-controlled entity like a Google Group.



See the [IAM overview](https://docs.cloud.google.com/iam/docs/overview) to learn more about basic IAM concepts.

To invoke an authenticated Cloud Run function, the principal must have the invoker IAM **permission** :

  * `cloudfunctions.functions.invoke`. This is usually through the [Invoker role](https://docs.cloud.google.com/functions/docs/reference/iam/roles#cloudfunctions.invoker).



To grant these permissions, use the [`add-invoker-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/add-invoker-policy-binding) command, as shown in Authenticating function to function calls.

For permission to create, update, or perform other administrative actions on a function, the principal must have an appropriate **role**. Roles include permissions that define the actions that the principal is allowed to do. See [Using IAM to Authorize Access](https://docs.cloud.google.com/functions/1stgendocs/securing/managing-access-iam) for more information.

Invoking a function can have additional complexities. [Event-driven functions](https://docs.cloud.google.com/functions/1stgendocs/writing#event-driven_functions) can only be invoked by the event source to which they are subscribed, but [HTTP functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-http-functions) can be invoked by different kinds of identities, originating in different places. The invoker might be a developer who is testing the function or another function or service that wishes to use the function. By default, these identities must provide an **ID token** with the request to authenticate themselves. In addition, the account being used must also have been granted the appropriate permissions.

Learn more about generating and using ID tokens.

**Note:** All functions can be invoked by using the [call API](https://docs.cloud.google.com/functions/1stgendocs/running/direct). You should only use this API for testing purposes. Do **not** use it in production.

## Authentication examples

This section shows a few different examples of authenticating for invocation.

### Example 1: Authenticate developer testing

As a developer, you need access to create, update, and delete functions, and this is granted using the [normal (IAM) process](https://docs.cloud.google.com/functions/1stgendocs/securing/managing-access-iam#adding_principals_and_granting_roles).

But as a developer, you might need to **invoke** your functions for testing purposes. To invoke a function using `curl` or similar tools, note the following:

  * Assign a role to your Cloud Run functions user account that contains the invoke permission.

    * `cloudfunctions.functions.invoke`. This is usually through the [Invoker role](https://docs.cloud.google.com/functions/docs/reference/iam/roles#cloudfunctions.invoker). By default, the _Cloud Run functions Admin_ and _Cloud Run functions Developer_ roles have this permission. See [Cloud Run functions IAM Roles](https://docs.cloud.google.com/functions/docs/reference/iam/roles) for the full list of roles and their associated permissions.
  * If you are working from your local machine, set up command-line access by [initializing](https://docs.cloud.google.com/sdk/docs/initialize) the Google Cloud CLI.

  * Provide your request with authentication credentials as a Google-generated ID token stored in an `Authorization` header. For example, get an ID token using `gcloud` by running the following command:
        
        curl  -H "Authorization: Bearer $(gcloud auth print-identity-token)" \
          https://FUNCTION_URL

where FUNCTION_URL is the URL of your function. Retrieve this URL from the Cloud Run functions page of the Google Cloud console or by running the [`gcloud functions describe`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/describe) command as shown in the first step of the [Google Cloud CLI deployment command](https://docs.cloud.google.com/functions/1stgendocs/create-deploy-gcloud-1st-gen#test_the_function) example.




You can use tokens created by `gcloud` to invoke HTTP functions in any project as long as your account has the `cloudfunctions.functions.invoke` permission on the function being invoked. For development purposes, use `gcloud`-generated ID tokens. However, note that such tokens lack an audience claim, which makes them susceptible to relay attacks. In production environments, use ID tokens issued for a service account with the appropriate audience specified. This approach enhances security by restricting token usage to the intended service only.

As always, we recommend that you allocate the [minimum set of permissions](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#limit-service-account-privileges) required to develop and use your functions. Make sure that IAM policies on your functions are limited to the minimum number of users and service accounts.

### Example 2: Authenticate function to function calls

When building services that connect multiple functions, it's a good idea to ensure that each function can only send requests to a specific subset of your other functions. For example, if you have a `login` function, it should be able to access the `user profiles` function, but it probably shouldn't be able to access the `search` function.

To configure the receiving function to accept requests from a specific calling function, you need to grant the appropriate invoker role to the calling function's service account on the receiving function. The invoker role is Cloud Run functions Invoker (`roles/cloudfunctions.invoker`):

### Console

Use the Cloud Run functions Invoker:

  1. Go to the Google Cloud console: 

[Go to Google Cloud console](https://console.cloud.google.com/functions/)

  2. Click the checkbox next to the receiving function. (Don't click the function itself.)

  3. Click **Permissions** at the top of the screen. The **Permissions** panel opens.

  4. Click **Add principal**.

  5. In the **New principals** field, enter the identity of the calling function. This should be a service account email.

  6. Select the role **Cloud Functions > Cloud Functions Invoker** from the **Select a role** drop-down menu.

  7. Click **Save**.




###  gcloud 

Use the `gcloud functions add-invoker-policy-binding` command:
    
    
    gcloud functions add-invoker-policy-binding RECEIVING_FUNCTION \
      --member='serviceAccount:CALLING_FUNCTION_IDENTITY'

The [`add-invoker-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/add-invoker-policy-binding) command adds an invoker role IAM policy binding that allows the specified member (principal) to invoke the specified function. Google Cloud CLI automatically detects the function generation and adds the correct Invoker role (`cloudfunctions.invoker` for 1st gen).

Replace the following:

  * `RECEIVING_FUNCTION`: The name of the receiving function.
  * `CALLING_FUNCTION_IDENTITY`: The calling function identity, a service account email.



Because it will be invoking the receiving function, the calling function must also provide a Google-signed ID token to authenticate. This is a two step process:

  1. Create a Google-signed ID token with the audience field (`aud`) set to the URL of the receiving function.

  2. Include the ID token in an `Authorization: Bearer ID_TOKEN` header in the request to the function.




By far the easiest and most reliable way to manage this process is to use the authentication libraries, as shown below, to generate and employ this token.

## Generate ID tokens

This section describes different ways you can generate the ID token a principal needs to invoke a function.

Unauthenticated access without an ID token is possible, but must be enabled. See [Using IAM to Authorize Access](https://docs.cloud.google.com/functions/1stgendocs/securing/managing-access-iam#allowing_unauthenticated_http_function_invocation) for more information.

**Note:** ID tokens also contain information about the identity they represent. To access that information, you can use [widely available libraries](https://jwt.io/libraries).

### Generate tokens programmatically

After the following code generates an ID token, it calls your Cloud Run function with that token on your behalf. This code works in any environment where the libraries can obtain authentication credentials, including environments that support local [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/production#automatically).

###  Node.js 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    
    // Cloud Functions uses your function's url as the `targetAudience` value
    // const targetAudience = 'https://project-region-projectid.cloudfunctions.net/myFunction';
    // For Cloud Functions, endpoint (`url`) and `targetAudience` should be equal
    // const url = targetAudience;
    
    
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
    
        # Cloud Functions uses your function's URL as the `audience` value
        # audience = https://project-region-projectid.cloudfunctions.net/myFunction
        # For Cloud Functions, `endpoint` and `audience` should be equal
    
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
    	// For Cloud Functions, endpoint (`serviceUrl`) and `audience` are the same.
    	// Example `audience` value (Cloud Functions): https://<PROJECT>-<REGION>-<PROJECT_ID>.cloudfunctions.net/myFunction
    	// (`targetURL` and `audience` will differ for GET parameters)
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
      // For Cloud Functions, endpoint (`serviceUrl`) and `audience` are the same.
      // Example `audience` value (Cloud Functions): https://project-region-projectid.cloudfunctions.net/myFunction
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

### Generate tokens manually

If you're invoking a function and for some reason you cannot use the authentication libraries, there are two ways you can get the ID token manually, either using the [Compute metadata server](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata) or by creating a self-signed JWT and exchanging it for a Google-signed ID token.

**Note:** For other ways to get this token, see [Methods for getting an ID token](https://docs.cloud.google.com/docs/authentication/get-id-token#methods).

#### Use the metadata server

You can use the Compute metadata server to fetch ID tokens with a specific audience as follows:
    
    
    curl "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/identity?audience=AUDIENCE" \
         -H "Metadata-Flavor: Google"
    

Replace AUDIENCE with the URL of the function you are invoking. You can retrieve this URL as described in the Authenticating developer testing section above.

**Note:** This method does not work from a local machine.

#### Exchange a self-signed JWT for a Google-signed ID token

  1. Grant the Invoker (`roles/cloudfunctions.invoker`) role to the calling function's service account on the receiving function.

  2. Create a [service account and a key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys) and download the file with the private key (in JSON format) to the host from which the calling function or service makes its requests.

  3. Create a [JWT](https://en.wikipedia.org/wiki/JSON_Web_Token) with the header set to `{"alg":"RS256","typ":"JWT"}`. The payload should include a `target_audience` claim set to the URL of the receiving function and `iss` and `sub` claims set to the email address of the service account used above. It should also include `exp`, and `iat` claims. The `aud` claim should be set to `https://www.googleapis.com/oauth2/v4/token`.

  4. Use the private key downloaded above to sign the JWT.

  5. Using this JWT, send a POST request to https://www.googleapis.com/oauth2/v4/token. Authentication data must be included in the header and the body of the request.

In the header:
         
         Authorization: Bearer $JWT - where $JWT is the JWT you just created
         Content-Type: application/x-www-form-urlencoded
         

In the body:
         
         grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer&assertion=$JWT
         

Replace `$JWT` with the JWT you just created

This returns _another_ JWT which includes an `id_token` signed by Google.




Send your GET/POST request to the receiving function. Include the Google-signed ID token in an `Authorization: Bearer ID_TOKEN_JWT` header in the request.

**Note:** A Google-signed ID token expires one hour from the request that initially generates it.

## What's next

  * Learn how to [manage access](https://docs.cloud.google.com/functions/1stgendocs/securing/managing-access-iam) to functions.

  * Get help with [other ways to generate ID tokens](https://docs.cloud.google.com/docs/authentication/get-id-token).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
