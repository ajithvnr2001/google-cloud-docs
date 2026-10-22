---
url: https://docs.cloud.google.com/recaptcha/docs/create-assessment-website/
title: Create assessments for websites \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:09.208614+00:00
---

# Create assessments for websites  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/create-assessment-website/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Create assessments for websites Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to create an assessment to allow your backend to verify the authenticity of the token that Google Cloud Fraud Defense sends. Fraud Defense sends an encrypted response, the response token (also known as a _token_), when the end user triggers an HTML action.

For any type of reCAPTCHA key integration (checkbox, score, or Universal), you must create an assessment to evaluate the results of `execute()` in your backend by submitting the generated token to the assessment endpoint. Fraud Defense processes the submitted token and reports the token's validity and score.

**Important:** For maximum security for your application, you should create assessments only on your backend. Otherwise, attackers can forge the request sent from the browser and make your application vulnerable to abuse and fraudulent activities. 

The first 10,000 Fraud Defense monthly assessments are free. To continue creating assessments after you reach the free monthly usage limit (10,000 assessments per month), you must enable billing for your Google Cloud project. For more information about billing for Fraud Defense, see [Billing information](https://docs.cloud.google.com/recaptcha/docs/billing-information).

## Before you begin

  1. [Prepare your environment for Google Cloud Fraud Defense](https://docs.cloud.google.com/recaptcha/docs/prepare-environment). 
  2. Ensure that you have the following Identity and Access Management role: reCAPTCHA Enterprise Agent (`roles/recaptchaenterprise.agent`).
  3. Install [score-based keys](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages), [checkbox keys](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages-with-checkbox), or [policy-based challenge keys](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages-policy) on your website.
  4. Set up authentication to Fraud Defense. 

The authentication method you choose depends on the environment where Fraud Defense is set up. The following table helps you choose the appropriate authentication method and the supported interface to set up authentication:

Environment | Interface | Authentication method  
---|---|---  
Google Cloud | 
     * REST
     * Client libraries
| Use [attached service accounts](https://docs.cloud.google.com/recaptcha/docs/authentication#on-gcp).  
On-premises or a different cloud provider | REST | Use [API keys](https://docs.cloud.google.com/docs/authentication/api-keys) or [Workload Identity Federation](https://docs.cloud.google.com/docs/authentication/set-up-adc-on-premises). If you want to use API keys, then we recommend securing the API keys by [applying API key restrictions](https://docs.cloud.google.com/docs/authentication/api-keys#api_key_restrictions).  
Client libraries | Use the following:
     * For Python or Java, use [API keys](https://docs.cloud.google.com/docs/authentication/api-keys) or [Workload Identity Federation](https://docs.cloud.google.com/docs/authentication/set-up-adc-on-premises). If you want to use API keys, then we recommend securing the API keys by [applying API key restrictions](https://docs.cloud.google.com/docs/authentication/api-keys#api_key_restrictions).
     * For other languages, use [Workload Identity Federation](https://docs.cloud.google.com/docs/authentication/set-up-adc-on-premises).  



## Retrieve a token

Retrieve a token from web pages in one of the following ways:

  * The resolved value of the promise returned by the call to `grecaptcha.enterprise.execute()`.
  * Use the `g-recaptcha-response` POST parameter when a user submits a form on your site.
  * As a string argument to your callback function if `data-callback` is specified in either the `g-recaptcha` [HTML tag attribute](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages-with-checkbox#automatically_render_the_widget) or the [callback parameter](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages-with-checkbox#explicitly_render_the_widget) in the `grecaptcha.enterprise.render` method.



You can access each user's token only _once_. If you need to assess a subsequent action that a user takes on your site, or if a token expires before an assessment is created, you must call `execute()` again to generate a new token.

**Note:** Each token can be used only once, and it expires after two minutes. 

## Create an assessment

After you set up authentication, create an assessment by sending a request to the reCAPTCHA Enterprise API or by using the reCAPTCHA Client Libraries.

To improve detection, we recommend that you pass the following additional values when creating assessments: 

  * `userAgent`: The user agent is included in the HTTP request in the request header. For more information, see [Learn about the `User-Agent` request header in the Mozilla Developer Network documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent).
  * `userIpAddress`: The IP address of the user sending a request to your backend is available in the HTTP request. If you use a proxy server, the IP address is available in the `X-Forwarded-For` request header. For more information about getting the IP address, see [`X-Forwarded-For`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For). 
  * `ja4`: JA4 is an open source method for fingerprinting TLS clients. For more information about how to create a JA4 fingerprint, see the [JA4 documentation on GitHub](https://github.com/FoxIO-LLC/ja4).
  * `ja3`: JA3 is an open source method for fingerprinting TLS clients. For more information about how to create a JA3 fingerprint, see the [JA3 documentation on GitHub](https://github.com/salesforce/ja3).



This helps in protecting your website and mobile applications against advanced attack patterns and human-led abuse.

To learn more about how Fraud Defense handles data, see [Is Fraud Defense GDPR compliant?](https://docs.cloud.google.com/recaptcha/docs/faq#gdpr-compliance) and [GDPR at Google - Privacy, Safety & Security](https://cloud.google.com/privacy/gdpr).

The way you create an assessment is the same for score-based keys, checkbox keys, policy-based challenge keys, and Universal keys.

### REST API

Create an assessment by sending a request to the reCAPTCHA API. You can use either the gcloud CLI or an API key for authentication. 

#### Use the gcloud CLI

Create an assessment using the [`projects.assessments.create`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments/create) method. Send this request to the `v1` API endpoint.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * TOKEN: token returned from the `grecaptcha.enterprise.execute()` call
  * KEY_ID: the reCAPTCHA key associated with the site or app. For more information, see [reCAPTCHA keys](https://docs.cloud.google.com/recaptcha/docs/keys).
  * USER_AGENT: the user agent in the request from the user's device.
  * USER_IP_ADDRESS: the IP address in the request from the user's device.
  * JA4: JA4 fingerprint for the TLS client. We recommend using [`FoxIO-LLC/ja4`](https://github.com/FoxIO-LLC/ja4) for computing the JA4 fingerprint.
  * JA3: JA3 fingerprint for the TLS client. We recommend using [`salesforce/ja3`](https://github.com/salesforce/ja3) for computing the JA3 fingerprint.
  * USER_ACTION: the user-initiated action that you specified for `action` in the `grecaptcha.enterprise.execute()` call, such as `login`. 

For more information, see [Action names](https://docs.cloud.google.com/recaptcha/docs/actions-website). **Note:** Actions are not supported for the checkbox key integrations that render widgets explicitly. 




HTTP method and URL: 
    
    
    POST https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/assessments

Request JSON body: 
    
    
    {
      "event": {
        "token": "TOKEN",
        "siteKey": "KEY_ID",
        "userAgent": "USER_AGENT",
        "userIpAddress": "USER_IP_ADDRESS",
        "ja4": "JA4",
        "ja3": "JA3",
        "expectedAction": "USER_ACTION"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/assessments"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/assessments" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "tokenProperties": {
        "valid": true,
        "hostname": "www.google.com",
        "action": "homepage",
        "createTime": "2019-03-28T12:24:17.894Z"
      },
      "riskAnalysis": {
        "score": 0.1,
        "reasons": ["AUTOMATION"]
      },
     "event": {
        "token": "TOKEN",
        "siteKey": "KEY_ID",
        "userAgent": "USER_AGENT",
        "userIpAddress": "USER_IP_ADDRESS",
        "ja4": "JA4",
        "ja3": "JA3",
        "expectedAction": "USER_ACTION"
      },
      "name": "projects/PROJECT_NUMBER/assessments/b6ac310000000000"
    }
    

**Note:** For integrations with actions, verify that the return value of `action` matches `expectedAction` when calling the `projects.assessments.create` method. If there is a mismatch, it indicates that an attacker is attempting to falsify actions. You can take actions against the user interaction, such as adding additional verifications or blocking the interaction to prevent any fraudulent activities. 

We recommend using a non-strict parsing mode in your JSON parser to prevent outages if additional fields are introduced in the response. 

#### Use an API key

Create an assessment using the [`projects.assessments.create`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments/create) method. Send this request to the `v1` API endpoint.

**Note:** If you are using the `v1beta1` version of the API, we recommend using the `v1` version because the new features, such as reCAPTCHA account defender, are available only on the `v1` version. For migrating from `v1beta1` to `v1`, see [Migrate from v1beta API to v1 API](https://docs.cloud.google.com/recaptcha/docs/migration-v1). 

Before using any of the request data, make the following replacements: 

  * API_KEY: API key associated with the current project
  * PROJECT_ID: your Google Cloud project ID
  * TOKEN: token returned from the `grecaptcha.enterprise.execute()` call
  * KEY_ID: the reCAPTCHA key associated with the site or app. For more information, see [reCAPTCHA keys](https://docs.cloud.google.com/recaptcha/docs/keys).
  * USER_AGENT: the user agent in the request from the user's device.
  * USER_IP_ADDRESS: the IP address in the request from the user's device.
  * JA3: JA3 fingerprint for the SSL client. We recommend using [salesforce/ja3](https://github.com/salesforce/ja3) for computing JA3.
  * USER_ACTION: the user-initiated action that you specified for `action` in the `grecaptcha.enterprise.execute()` call, such as `login`. 

For more information, see [Action names](https://docs.cloud.google.com/recaptcha/docs/actions-website). **Note:** Actions are not supported for the checkbox key integrations that render widgets explicitly. 




HTTP method and URL: 
    
    
    POST https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/assessments?key=API_KEY

Request JSON body: 
    
    
    {
      "event": {
        "token": "TOKEN",
        "siteKey": "KEY_ID",
        "userAgent": "USER_AGENT",
        "userIpAddress": "USER_IP_ADDRESS",
        "ja3": "JA3",
        "expectedAction": "USER_ACTION"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** Create an [API key](https://cloud.google.com/docs/authentication/api-keys#creating_an_api_key) to authenticate with the API. 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/assessments?key=API_KEY"

#### PowerShell

**Note:** Create an [API key](https://cloud.google.com/docs/authentication/api-keys#creating_an_api_key) to authenticate with the API. 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $headers = @{  }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/assessments?key=API_KEY" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "tokenProperties": {
        "valid": true,
        "hostname": "www.google.com",
        "action": "homepage",
        "createTime": "2019-03-28T12:24:17.894Z"
      },
      "riskAnalysis": {
        "score": 0.1,
        "reasons": ["AUTOMATION"]
      },
      "event": {
        "token": "TOKEN",
        "siteKey": "KEY_ID",
        "userAgent": "USER_AGENT",
        "userIpAddress": "USER_IP_ADDRESS",
        "ja3": "JA3",
        "expectedAction": "USER_ACTION"
      },
      "name": "projects/PROJECT_NUMBER/assessments/b6ac310000000000"
    }
    

**Note:** For integrations with actions, verify that the return value of `action` matches `expectedAction` when calling the `projects.assessments.create` method. If there is a mismatch, it indicates that an attacker is attempting to falsify actions. You can take actions against the user interaction, such as adding additional verifications or blocking the interaction to prevent any fraudulent activities. 

We recommend using a non-strict parsing mode in your JSON parser to prevent outages if additional fields are introduced in the response. 

### C#
    
    
      using System;
      using Google.Api.Gax.ResourceNames;
      using Google.Cloud.RecaptchaEnterprise.V1;
    
      public class CreateAssessmentSample
      {
          // Create an assessment to analyze the risk of a UI action.
          // projectID: Google Cloud project ID.
          // recaptchaKey: reCAPTCHA key obtained by registering a domain or an app to use reCAPTCHA Enterprise.
          // token: The token obtained from the client on passing the recaptchaKey.
          // recaptchaAction: Action name corresponding to the token.
          public void createAssessment(string projectID = "project-id", string recaptchaKey = "recaptcha-key",
              string token = "action-token", string recaptchaAction = "action-name")
          {
    
              // Create the client.
              // TODO: To avoid memory issues, move this client generation outside
              // of this example, and cache it (recommended) or call client.close()
              // before exiting this method.
              RecaptchaEnterpriseServiceClient client = RecaptchaEnterpriseServiceClient.Create();
    
              ProjectName projectName = new ProjectName(projectID);
    
              // Build the assessment request.
              CreateAssessmentRequest createAssessmentRequest = new CreateAssessmentRequest()
              {
                  Assessment = new Assessment()
                  {
                      // Set the properties of the event to be tracked.
                      Event = new Event()
                      {
                          SiteKey = recaptchaKey,
                          Token = token,
                          ExpectedAction = recaptchaAction
                      },
                  },
                  ParentAsProjectName = projectName
              };
    
              Assessment response = client.CreateAssessment(createAssessmentRequest);
    
              // Check if the token is valid.
              if (response.TokenProperties.Valid == false)
              {
                  System.Console.WriteLine("The CreateAssessment call failed because the token was: " +
                      response.TokenProperties.InvalidReason.ToString());
                  return;
              }
    
              // Check if the expected action was executed.
              if (response.TokenProperties.Action != recaptchaAction)
              {
                  System.Console.WriteLine("The action attribute in the reCAPTCHA tag is: " +
                      response.TokenProperties.Action.ToString());
                  System.Console.WriteLine("The action attribute in the reCAPTCHA tag does not " +
                      "match the action you are expecting to score");
                  return;
              }
    
              // Get the risk score and the reasons.
              // For more information on interpreting the assessment,
              // see: https://cloud.google.com/recaptcha/docs/interpret-assessment
              System.Console.WriteLine("The reCAPTCHA score is: " + ((decimal)response.RiskAnalysis.Score));
    
              foreach (RiskAnalysis.Types.ClassificationReason reason in response.RiskAnalysis.Reasons)
              {
                  System.Console.WriteLine(reason.ToString());
              }
          }
    
          public static void Main(string[] args)
          {
              new CreateAssessmentSample().createAssessment();
          }
      }

### Go
    
    
      import (
        "context"
        "fmt"
    
        recaptcha "cloud.google.com/go/recaptchaenterprise/v2/apiv1"
        recaptchapb "cloud.google.com/go/recaptchaenterprise/v2/apiv1/recaptchaenterprisepb"
      )
    
      func main() {
        // TODO(developer): Replace these variables before running the sample.
        projectID := "project-id"
        recaptchaKey := "recaptcha-key"
        token := "action-token"
        recaptchaAction := "action-name"
    
        createAssessment(projectID, recaptchaKey, token, recaptchaAction)
      }
    
      /**
      * Create an assessment to analyze the risk of a UI action.
      *
      * @param projectID: Google Cloud project ID
      * @param recaptchaKey: reCAPTCHA key obtained by registering a domain or an app to use the services of Fraud Defense.
      * @param token: The token obtained from the client on passing the `recaptchaKey`.
      * @param recaptchaAction: Action name corresponding to the token.
      */
      func createAssessment(projectID string, recaptchaKey string, token string, recaptchaAction string) {
    
        // Create the recaptcha client.
        // TODO: To avoid memory issues, move this client generation outside
        // of this example, and cache it (recommended) or call client.close()
        // before exiting this method.
        ctx := context.Background()
        client, err := recaptcha.NewClient(ctx)
        if err != nil {
          fmt.Printf("Error creating reCAPTCHA client\n")
        }
        defer client.Close()
    
        // Set the properties of the event to be tracked.
        event := &recaptchapb.Event{
          Token:          token,
          SiteKey:        recaptchaKey,
        }
    
        assessment := &recaptchapb.Assessment{
          Event: event,
        }
    
        // Build the assessment request.
        request := &recaptchapb.CreateAssessmentRequest{
          Assessment: assessment,
          Parent:     fmt.Sprintf("projects/%s", projectID),
        }
    
        response, err := client.CreateAssessment(
          ctx,
          request)
    
        if err != nil {
          fmt.Printf("%v", err.Error())
        }
    
        // Check if the token is valid.
        if response.TokenProperties.Valid == false {
          fmt.Printf("The CreateAssessment() call failed because the token"+
             " was invalid for the following reasons: %v",
          response.TokenProperties.InvalidReason)
          return
        }
    
        // Check if the expected action was executed.
        if response.TokenProperties.Action == recaptchaAction {
          // Get the risk score and the reason(s).
          // For more information on interpreting the assessment,
          // see: https://cloud.google.com/recaptcha/docs/interpret-assessment
          fmt.Printf("The reCAPTCHA score for this token is:  %v",
            response.RiskAnalysis.Score)
    
          for _,reason := range response.RiskAnalysis.Reasons {
            fmt.Printf(reason.String()+"\n")
          }
          return
        }
    
        fmt.Printf("The action attribute in your reCAPTCHA tag does " +
            "not match the action you are expecting to score")
      }

### Java
    
    
    import com.google.cloud.recaptchaenterprise.v1.[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html);
    import com.google.recaptchaenterprise.v1.[Assessment](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html);
    import com.google.recaptchaenterprise.v1.[CreateAssessmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.CreateAssessmentRequest.html);
    import com.google.recaptchaenterprise.v1.[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.html);
    import com.google.recaptchaenterprise.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ProjectName.html);
    import com.google.recaptchaenterprise.v1.[RiskAnalysis](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.RiskAnalysis.html).[ClassificationReason](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.RiskAnalysis.ClassificationReason.html);
    import java.io.IOException;
    
    public class CreateAssessment {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectID = "project-id";
        String recaptchaSiteKey = "recaptcha-site-key";
        String token = "action-token";
        String recaptchaAction = "action-name";
        String userIpAddress = "user-ip-address";
        String userAgent = "user-agent";
        String ja3 = "ja3";
        String ja4 = "ja4";
    
        createAssessment(projectID, recaptchaSiteKey, token, recaptchaAction, userIpAddress, userAgent, ja3, ja4);
      }
    
      /**
       * Create an assessment to analyze the risk of an UI action. Assessment approach is the same for
       * both 'score' and 'checkbox' type recaptcha site keys.
       *
       * @param projectID : GCloud Project ID
       * @param recaptchaSiteKey : Site key obtained by registering a domain/app to use recaptcha
       *     services. (score/ checkbox type)
       * @param token : The token obtained from the client on passing the recaptchaSiteKey.
       * @param recaptchaAction : Action name corresponding to the token.
       * @param userIpAddress: IP address of the user sending a request.
       * @param userAgent: User agent is included in the HTTP request in the request header. 
       * @param ja3: JA3 associated with the request.
       * @param ja4: JA4 associated with the request.
       */
      public static void createAssessment(
          String projectID, String recaptchaSiteKey, String token, String recaptchaAction, String userIpAddress, String userAgent, String ja3, String ja4)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `client.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html) client = [RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html).create()) {
    
          // Set the properties of the event to be tracked.
          [Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.html) event = [Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.html).newBuilder()
              .[setSiteKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.Builder.html#com_google_recaptchaenterprise_v1_Event_Builder_setSiteKey_java_lang_String_)(recaptchaSiteKey)
              .[setToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.Builder.html#com_google_recaptchaenterprise_v1_Event_Builder_setToken_java_lang_String_)(token)
              .[setUserIpAddress](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.Builder.html#com_google_recaptchaenterprise_v1_Event_Builder_setUserIpAddress_java_lang_String_)(userIpAddress)
              .[setJa3](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.Builder.html#com_google_recaptchaenterprise_v1_Event_Builder_setJa3_java_lang_String_)(ja3)
              .[setJa4](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.Builder.html#com_google_recaptchaenterprise_v1_Event_Builder_setJa4_java_lang_String_)(ja4)
              .[setUserAgent](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Event.Builder.html#com_google_recaptchaenterprise_v1_Event_Builder_setUserAgent_java_lang_String_)(userAgent)
              .build();
    
          // Build the assessment request.
          [CreateAssessmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.CreateAssessmentRequest.html) createAssessmentRequest =
              [CreateAssessmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.CreateAssessmentRequest.html).newBuilder()
                  .setParent([ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ProjectName.html).of(projectID).toString())
                  .setAssessment([Assessment](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html).newBuilder().[setEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.Builder.html#com_google_recaptchaenterprise_v1_Assessment_Builder_setEvent_com_google_recaptchaenterprise_v1_Event_)(event).build())
                  .build();
    
          [Assessment](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html) response = client.createAssessment(createAssessmentRequest);
    
          // Check if the token is valid.
          if (!response.[getTokenProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html#com_google_recaptchaenterprise_v1_Assessment_getTokenProperties__)().getValid()) {
            System.out.println(
                "The CreateAssessment call failed because the token was: "
                    + response.[getTokenProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html#com_google_recaptchaenterprise_v1_Assessment_getTokenProperties__)().getInvalidReason().name());
            return;
          }
    
          // Check if the expected action was executed.
          // (If the key is checkbox type and 'action' attribute wasn't set, skip this check.)
          if (!response.[getTokenProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html#com_google_recaptchaenterprise_v1_Assessment_getTokenProperties__)().getAction().equals(recaptchaAction)) {
            System.out.println(
                "The action attribute in reCAPTCHA tag is: "
                    + response.[getTokenProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html#com_google_recaptchaenterprise_v1_Assessment_getTokenProperties__)().getAction());
            System.out.println(
                "The action attribute in the reCAPTCHA tag "
                    + "does not match the action ("
                    + recaptchaAction
                    + ") you are expecting to score");
            return;
          }
    
          // Get the reason(s) and the risk score.
          // For more information on interpreting the assessment,
          // see: https://cloud.google.com/recaptcha-enterprise/docs/interpret-assessment
          for ([ClassificationReason](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.RiskAnalysis.ClassificationReason.html) reason : response.[getRiskAnalysis](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html#com_google_recaptchaenterprise_v1_Assessment_getRiskAnalysis__)().getReasonsList()) {
            System.out.println(reason);
          }
    
          float recaptchaScore = response.[getRiskAnalysis](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html#com_google_recaptchaenterprise_v1_Assessment_getRiskAnalysis__)().getScore();
          System.out.println("The reCAPTCHA score is: " + recaptchaScore);
    
          // Get the assessment name (id). Use this to annotate the assessment.
          String assessmentName = response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment.html#com_google_recaptchaenterprise_v1_Assessment_getName__)();
          System.out.println(
              "Assessment name: " + assessmentName.substring(assessmentName.lastIndexOf("/") + 1));
        }
      }
    }

### Node.js
    
    
      const {RecaptchaEnterpriseServiceClient} =
          require('@google-cloud/recaptcha-enterprise');
    
     /**
     * Create an assessment to analyze the risk of a UI action. Note that
     * this example does set error boundaries and returns `null` for
     * exceptions.
     *
     * projectID: Google Cloud project ID
     * recaptchaKey: reCAPTCHA key obtained by registering a domain or an app to use the services of Fraud Defense.
     * token: The token obtained from the client on passing the `recaptchaKey`.
     * recaptchaAction: Action name corresponding to the token.
     * userIpAddress: The IP address of the user sending a request to your backend is available in the HTTP request.
     * userAgent: The user agent is included in the HTTP request in the request header.
     * ja4: JA4 fingerprint associated with the request.
     * ja3: JA3 fingerprint associated with the request.
     */
     async function createAssessment({
       projectID = "your-project-id",
       recaptchaKey = "your-recaptcha-key",
       token = "action-token",
       recaptchaAction = "action-name",
       userIpAddress = "user-ip-address",
       userAgent = "user-agent",
       ja4 = "ja4",
       ja3 = "ja3"
     }) {
       // Create the reCAPTCHA client & set the project path. There are multiple
       // ways to authenticate your client. For more information see:
       // https://cloud.google.com/docs/authentication
       // TODO: To avoid memory issues, move this client generation outside
       // of this example, and cache it (recommended) or call client.close()
       // before exiting this method.
       const client = new RecaptchaEnterpriseServiceClient();
       const projectPath = client.projectPath(projectID);
    
       // Build the assessment request.
       const request = ({
         assessment: {
           event: {
             token: token,
             siteKey: recaptchaKey,
             userIpAddress: userIpAddress,
             userAgent: userAgent,
             ja4: ja4,
             ja3: ja3,
           },
         },
         parent: projectPath,
       });
    
       // client.createAssessment() can return a Promise or take a Callback
       const [ response ] = await client.createAssessment(request);
    
       // Check if the token is valid.
       if (!response.tokenProperties.valid) {
        console.log("The CreateAssessment call failed because the token was: " +
          response.tokenProperties.invalidReason);
    
        return null;
       }
    
       // Check if the expected action was executed.
       // The `action` property is set by the user client in the
       // grecaptcha.enterprise.execute() method.
       if (response.tokenProperties.action === recaptchaAction) {
    
        // Get the risk score and the reason(s).
        // For more information on interpreting the assessment,
        // see: https://cloud.google.com/recaptcha/docs/interpret-assessment
        console.log("The reCAPTCHA score is: " +
          response.riskAnalysis.score);
    
        response.riskAnalysis.reasons.forEach((reason) => {
          console.log(reason);
        });
        return response.riskAnalysis.score;
       } else {
        console.log("The action attribute in your reCAPTCHA tag " +
          "does not match the action you are expecting to score");
        return null;
       }
     }

### PHP
    
    
      <?php
    
      // Include Google Cloud dependencies using Composer
      // composer require google/cloud-recaptcha-enterprise
      require 'vendor/autoload.php';
    
      use Google\Cloud\RecaptchaEnterprise\V1\Client\RecaptchaEnterpriseServiceClient;
      use Google\Cloud\RecaptchaEnterprise\V1\Event;
      use Google\Cloud\RecaptchaEnterprise\V1\Assessment;
      use Google\Cloud\RecaptchaEnterprise\V1\CreateAssessmentRequest;
      use Google\Cloud\RecaptchaEnterprise\V1\TokenProperties\InvalidReason;
    
      /**
      * Create an assessment to analyze the risk of a UI action.
      * @param string $siteKey The key ID for the reCAPTCHA key (See https://cloud.google.com/recaptcha/docs/create-key)
      * @param string $token The user's response token for which you want to receive a reCAPTCHA score. (See https://cloud.google.com/recaptcha/docs/create-assessment#retrieve_token)
      * @param string $project Your Google Cloud project ID
      */
      function create_assessment(
         string $siteKey,
         string $token,
         string $project
      ): void {
      // TODO: To avoid memory issues, move this client generation outside
      // of this example, and cache it (recommended) or call client.close()
      // before exiting this method.
      $client = new RecaptchaEnterpriseServiceClient();
      $projectName = $client->projectName($project);
    
         $event = (new Event())
             ->setSiteKey($siteKey)
             ->setToken($token);
    
         $assessment = (new Assessment())
             ->setEvent($event);
    
         $request = (new CreateAssessmentRequest())
             ->setParent($projectName)
             ->setAssessment($assessment);
    
         try {
             $response = $client->createAssessment($request);
    
             // You can use the score only if the assessment is valid,
             // In case of failures like re-submitting the same token, getValid() will return false
             if ($response->getTokenProperties()->getValid() == false) {
                 printf('The CreateAssessment() call failed because the token was invalid for the following reason: ');
                 printf(InvalidReason::name($response->getTokenProperties()->getInvalidReason()));
             } else {
                 printf('The score for the protection action is:');
                 printf($response->getRiskAnalysis()->getScore());
    
                 // Optional: You can use the following methods to get more data about the token
                 // Action name provided at token generation.
                 // printf($response->getTokenProperties()->getAction() . PHP_EOL);
                 // The timestamp corresponding to the generation of the token.
                 // printf($response->getTokenProperties()->getCreateTime()->getSeconds() . PHP_EOL);
                 // The hostname of the page on which the token was generated.
                 // printf($response->getTokenProperties()->getHostname() . PHP_EOL);
             }
         } catch (exception $e) {
             printf('CreateAssessment() call failed with the following error: ');
             printf($e);
         }
      }
    
      // TODO(Developer): Replace the following before running the sample
      create_assessment(
         'YOUR_RECAPTCHA_KEY',
         'YOUR_USER_RESPONSE_TOKEN',
         'YOUR_GOOGLE_CLOUD_PROJECT_ID'
      );
    ?>

### Python
    
    
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    from google.cloud.recaptchaenterprise_v1 import [Assessment](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Assessment.html)
    
    
    def create_assessment(
        project_id: str,
        recaptcha_site_key: str,
        token: str,
        recaptcha_action: str,
        user_ip_address: str,
        user_agent: str,
        ja3: str,
    ) -> Assessment:
        """Create an assessment to analyze the risk of a UI action.
        Args:
            project_id: GCloud Project ID
            recaptcha_site_key: Site key obtained by registering a domain/app to use recaptcha services.
            token: The token obtained from the client on passing the recaptchaSiteKey.
            recaptcha_action: Action name corresponding to the token.
            user_ip_address: IP address of the user sending a request.
            user_agent: User agent is included in the HTTP request in the request header.
            ja3: JA3 associated with the request.
        """
    
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Set the properties of the event to be tracked.
        event = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[Event](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Event.html)()
        event.site_key = recaptcha_site_key
        event.token = token
        event.user_ip_address = user_ip_address
        event.user_agent = user_agent
        event.ja3 = ja3
    
        assessment = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[Assessment](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Assessment.html)()
        assessment.event = event
    
        project_name = f"projects/{project_id}"
    
        # Build the assessment request.
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[CreateAssessmentRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.CreateAssessmentRequest.html)()
        request.assessment = assessment
        request.parent = project_name
    
        response = client.[create_assessment](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_create_assessment)(request)
    
        # Check if the token is valid.
        if not response.token_properties.valid:
            print(
                "The CreateAssessment call failed because the token was "
                + "invalid for for the following reasons: "
                + str(response.token_properties.invalid_reason)
            )
            return
    
        # Check if the expected action was executed.
        if response.token_properties.action != recaptcha_action:
            print(
                "The action attribute in your reCAPTCHA tag does"
                + "not match the action you are expecting to score"
            )
            return
        else:
            # Get the risk score and the reason(s)
            # For more information on interpreting the assessment,
            # see: https://cloud.google.com/recaptcha-enterprise/docs/interpret-assessment
            for reason in response.risk_analysis.reasons:
                print(reason)
            print(
                "The reCAPTCHA score for this token is: "
                + str(response.risk_analysis.score)
            )
            # Get the assessment name (id). Use this to annotate the assessment.
            assessment_name = client.[parse_assessment_path](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_parse_assessment_path)(response.name).get("assessment")
            print(f"Assessment name: {assessment_name}")
        return response
    
    

### Ruby
    
    
    require "google/cloud/recaptcha_enterprise"
    
    # Create an assessment to analyze the risk of a UI action.
    #
    # @param site_key [String] Site key obtained by registering a domain/app to use recaptcha services.
    # @param token [String] The token obtained from the client on passing the recaptcha site_key.
    # @param project_id [String] GCloud Project ID.
    # @param recaptcha_action [String] Action name corresponding to the token.
    # @return [void]
    def create_assessment site_key:, token:, project_id:, recaptcha_action:
      # Create the reCAPTCHA client.
      client = ::Google::Cloud::RecaptchaEnterprise.recaptcha_enterprise_service
    
      request = { parent: "projects/#{project_id}",
                  assessment: {
                    event: {
                      site_key: site_key,
                      token: token
                    }
                  } }
    
      response = client.create_assessment request
    
      # Check if the token is valid.
      if !response.token_properties.valid
        puts "The create_assessment() call failed because the token was invalid with the following reason:" \
             "#{response.token_properties.invalid_reason}"
      # Check if the expected action was executed.
      elsif response.token_properties.action == recaptcha_action
        # Get the risk score and the reason(s).
        # For more information on interpreting the assessment,
        # see: https://cloud.google.com/recaptcha-enterprise/docs/interpret-assessment
        puts "The reCAPTCHA score for this token is: #{response.risk_analysis.score}"
        response.risk_analysis.reasons.each { |reason| puts reason }
      else
        puts "The action attribute in your reCAPTCHA tag does not match the action you are expecting to score"
      end
    end

**Note:** Your assessment's response might show `score=0.9` and `reason=LOW_CONFIDENCE`. This is because, after you integrate a new key on your frontend, Fraud Defense requires some time to return an accurate risk analysis. We recommend that you wait at least 48 hours before taking action on the returned scores. 

## What's next

  * [Interpret an assessment](https://docs.cloud.google.com/recaptcha/docs/interpret-assessment-website) and take an appropriate action for your site based on the score. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
