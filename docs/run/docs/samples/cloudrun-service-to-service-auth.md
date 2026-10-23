---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-service-to-service-auth/
title: Authenticate service-to-service requests \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:12.627836+00:00
---

# Authenticate service-to-service requests  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-service-to-service-auth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Authenticate service-to-service requests Stay organized with collections  Save and categorize content based on your preferences. 

Services hosted on Google Cloud with access to the Compute Metadata Server are able to generate an OAuth authentication token using the service account identity associated with the service. This token can be used to authenticate the service as a permitted invoker of a Cloud Run service.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Authenticating service-to-service](https://docs.cloud.google.com/run/docs/authenticating/service-to-service)



## Code sample

### Go

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

### Java

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Node.js

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Python

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

### Ruby

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "net/http"
    require "uri"
    require "googleauth"
    
    def make_get_request writer, target_url, audience
      credentials = Google::Auth.get_application_default target_audience: audience
      token_info = credentials.[fetch_access_token!](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-ExternalAccount-BaseCredentials.html)
      id_token = token_info["id_token"] if token_info
      raise "ID token is missing from credentials. Ensure you are using a service account or credentials that support ID tokens." if id_token.nil?
    
      uri = URI(target_url)
      request = Net::HTTP::Get.new uri
    
      request["Authorization"] = "Bearer #{id_token}"
    
      response = Net::HTTP.start uri.hostname, uri.port, use_ssl: uri.scheme == "https" do |http|
        http.open_timeout = 10
        http.read_timeout = 10
        http.request request
      end
    
      response.value
    
      writer.write response.body
    rescue StandardError => e
      raise "Failed to make get request: #{e.message}"
    end
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudrun). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
