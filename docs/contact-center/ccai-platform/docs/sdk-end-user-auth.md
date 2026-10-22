---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sdk-end-user-auth/
title: End user authentication \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:14.395996+00:00
---

# End user authentication  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sdk-end-user-auth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  End user authentication Stay organized with collections  Save and categorize content based on your preferences. 

Contact Center AI Platform uses end user authentication to securely identify the people using your host app. This mechanism ensures that only authorized users can access the CCAI Platform API and that their chat sessions and data remain securely tied to their specific identity.

To identify an end user, your host app must provide a universally unique identifier (UUID) that represents that specific person.

**Important:** **Don't use an email address as the identifier.** Email addresses can change and might not be unique. Using a UUID ensures CCAI Platform accurately tracks and differentiates the end user, even if their contact information changes over time.

## How authentication works in CCAI Platform

Authentication in CCAI Platform relies on a secure handshake using a [**JSON Web Token**](https://jwt.io/) **(JWT)**. A JWT is an open standard used to securely transmit information as a JSON object.

Here is the standard authentication flow:

  1. **The request** : When an end user starts using CCAI Platform customer service, the CCAI Platform SDK requests a signed JWT from your host app.

  2. **The signature** : Your host app signs the JWT using your shared CCAI Platform company secret (`company_secret`).

  3. **The exchange** : The host app passes the signed JWT back to the CCAI Platform SDK. The SDK then sends this JWT to the CCAI Platform server.

  4. **The verification** : The CCAI Platform server verifies the signature. If valid, CCAI Platform issues an auth token, granting the user access to the API and associating them with their account (or creating a new one if they don't exist).




If your host app doesn't provide an identifier in the JWT payload, CCAI Platform will create an anonymous guest account for the user.

## Prerequisites

Before implementing authentication, you need your unique SDK authentication elements. These securely identify your company to the CCAI Platform API.

  1. Sign into CCAI Platform with an administrator account.

  2. Navigate to **Settings** > **Developer Settings** > **API Credentials**.

  3. Locate your SDK key name (`sdk_key_name`), SDK key (`sdk_key`), and company secret (`company_secret`).




_Keep these credentials secure. Only share them with authorized systems and developers._

## Developer implementation guide

The following section outlines how developers should construct the JWT payload and initialize the CCAI Platform SDK across different platforms.

### JWT payload requirements

To pass the end user's information to CCAI Platform, your host app must construct a JWT payload. The callback method supplies a default payload (which may include a push token and default name), but you can add specific user details using the following reserved keys:

  * `identifier` (optional, but highly recommended UUID)

  * `name` (optional)

  * `email` (optional)

  * `phone` (optional, must use E.164 format)

  * `iss` (optional, your company name)

  * `iat` (required, issued at timestamp)

  * `exp` (required, expiration timestamp)




### Server-side signing (recommended)

**Important:** We strongly recommend signing the payload on your server. This keeps your `company_secret` hidden from the client side, preventing unauthorized access. If compromised, you can revoke the secret. In a production environment, you should also **ensure that the JWT signing algorithm used is appropriate for your security needs.**

#### API example on the server (Ruby on Rails)

This example shows how to sign the payload on the server-side using the Ruby on Rails framework with the [JWT gem](https://github.com/jwt/ruby-jwt).

The code sets up an API endpoint (`/api/ujet/sign`) using the `jwt` gem to encode the payload with a company secret and return the encoded token to the client.

Suppose the base URL of your host application is **https://company.com/api/**. To sign the payload for CCAI Platform, you can add another API endpoint at **https://company.com/api/ujet/sign**.

The code adds a new route to the application's routes file to handle POST requests to the `/api/ujet/sign` URL.

The `ujet_controller.rb` file defines the `UjetController` class, which has a single endpoint, **sign** , which is used to sign a payload for CCAI Platform.

In the code, the `COMPANY_SECRET` is defined as the secret used to sign the payload. The payload is extracted from the body of the request and then various values are added to it, for example, UNIQUE-IDENTIFIER, username, email, phone.

The `JWT.encode` method is used to encode the payload and the `ujet_secret` into a JSON Web Token (JWT), which is then returned in the response as a JSON object with the token key.
    
    
    # routes.rb
    post 'ujet/sign' => "ujet#sign"
    
    # ujet_controller.rb
    class UjetController
      def sign
        # In production, securely store and call your secret (e.g., via environment variables)
        ujet_secret = "COMPANY_SECRET"
    
        payload = body["payload"]
        payload["identifier"] = "UNIQUE-IDENTIFIER"
        payload["name"] = "user name"
        payload["email"] = "test@email.com"
        payload["phone"] = ""                     # E.164 format
        payload["iss"] = "YOUR_COMPANY_NAME"
        payload["iat"] = Time.now.to_i
        payload["exp"] = Time.now.to_i + 10.minutes # Valid for 10 minutes
    
        token = JWT.encode(payload, ujet_secret)
    
        render json: {token: token}
      end
    end
    

### Client-side initialization

Follow these guidelines to initialize your CCAI Platform mobile SDK.

#### Signing from the iOS SDK

This example of signing a payload from the iOS SDK makes a POST request to the server at the URL **https://your.company.com/api/ujet/sign** with the payload as the request body.

The server is expected to return a signed token in response, which is then passed to the success callback in the form of the "token" key in a JSON object.

If there is an error during the request, it is passed to the failure callback.
    
    
    -   (void)signPayload:(NSDictionary *)payload payloadType:(UjetPayloadType)payloadType success:(void (^)(NSString *))success failure:(void (^)(NSError *))failure
    {
      if (payloadType == UjetPayloadAuthToken) {
        NSURLSessionConfiguration *sessionConfiguration = [NSURLSessionConfiguration defaultSessionConfiguration];
        NSURLSession *session = [NSURLSession sessionWithConfiguration:sessionConfiguration];
    
        NSMutableURLRequest *mutableRequest = [[NSMutableURLRequest alloc] init];
        mutableRequest.URL = [NSURL URLWithString:@"https://your.company.com/api/ujet/sign"];
        mutableRequest.HTTPMethod = @"POST";
        NSError *error;
        NSDictionary *data = @{@"payload": payload};
        mutableRequest.HTTPBody = [NSJSONSerialization dataWithJSONObject:data options:0 error:&error];
    
        NSURLSessionDataTask *task = [session dataTaskWithRequest:mutableRequest completionHandler:^(NSData *data, NSURLResponse *response, NSError *error) {
            if(error) {
                failure(error);
            }
            else {
                NSDictionary *json = [NSJSONSerialization JSONObjectWithData:data options:0 error:nil];
                success(json[@"token"]);
            }
        }];
    
        [task resume];
      }
    }
    

#### Signing from the Android SDK

The following is an example of signing a payload from an Android SDK.

This example uses [Retrofit](https://github.com/square/retrofit), an HTTP client for Android, to request the signed payload from your server. The function takes a payload, a payload type, and a token callback as input.

If the payload type is `UjetPayloadType.AuthToken`, it creates a Retrofit instance, uses it to make a request to the `https://company.com/api` API endpoint to sign the payload, and returns the signed token in the `onToken` method of the `tokenCallback` instance.

In case of failure, it displays a toast message `"Authentication failed"`.
    
    
    public void onSignPayloadRequest(Map<String, Object> payload, UjetPayloadType ujetPayloadType, final UjetTokenCallback tokenCallback) {
        if (ujetPayloadType == UjetPayloadType.AuthToken) {
            Retrofit retrofit = new Retrofit.Builder()
                    .baseUrl("https://company.com/api/")
                    .addConverterFactory(GsonConverterFactory.create())
                    .build();
    
            AuthService authService = retrofit.create(AuthService.class);
            Call<AuthToken> authenticate = authService.authenticate(new AuthRequest(payload));
            authenticate.enqueue(new Callback<AuthToken>() {
                @Override
                public void onResponse(Call<AuthToken> call, Response<AuthToken> response) {
                    if (response.isSuccessful()) {
                        AuthToken authToken = response.body();
                        tokenCallback.onToken(authToken.getToken());
                    } else {
                        Toast.makeText(ExampleApplication.this, "Authentication failed", Toast.LENGTH_SHORT).show();
                    }
                }
    
                @Override
                public void onFailure(Call<AuthToken> call, Throwable t) {
                    Toast.makeText(ExampleApplication.this, "Authentication failed", Toast.LENGTH_SHORT).show();
                }
            });
        }
    }
    

#### Signing from the Web SDK

The following example demonstrates how to sign the payload in the Web SDK by making an API request to the server with the payload.

The server should be set up to handle the API request and sign the payload using a secure method. The result is then returned to the web page, which passes the signed token back to CCAI Platform using the callback function.
    
    
    $(function() {
      UJET.initialize({
        // ... other parameters
        handlers: {
          authentication(callback) {
            $.ajax({
              type: 'POST',
              url: 'https://company.com/api/ujet/sign',
              data: JSON.stringify({
                payload: {
                  identifier: 'UNIQUE-Identifier',
                  name: 'Test user'
                }
              }),
              success: function(result) {
                callback({
                  token: result.token,
                  user: {
                    identifier: 'UNIQUE-IDENTIFIER',
                    name: 'Test user'
                  }
                });
              }
            });
          }
        }
      }).then(function() {
        // successfully initialized
      }).catch(function(error) {
        // Handle initialization error
      });
    });
    

## Mid-session authentication and SDK reinitialization

In some cases, an end user may start a chat session as a guest (unauthenticated) and verify their identity mid-session (e.g., through a virtual assistant or a mid-flow login screen). To ensure the active session is securely updated and associated with the newly authenticated user, follow these steps:

### Steps for mid-session authentication

  1. **Initialize the SDK with a temporary identifier** : When the user isn't authenticated, initialize the CCAI Platform SDK using a random or guest identifier.

  2. **Direct the user to authenticate** : Guide the user into your authentication flow, such as a CCAI Platform virtual assistant (VA) or your app's built-in login screen.

  3. **Update the end user via API** : After the user successfully authenticates (and while they are still in the virtual agent or authentication flow), your backend must call the CCAI Platform Apps API to update the end user's chat session with their true identifier.

  4. **Reinitialize the SDK with a new JWT** : Upon a successful backend update, generate a new JWT for the authenticated user. Reinitialize the CCAI Platform SDK by calling the initialization method again with this new JWT.

  5. **Escalate the session (if using VA)** : If the user was authenticating using a virtual assistant, the virtual agent should now escalate the consumer to their final destination queue.




#### Example (Web SDK)

To reinitialize, call the `UJET.initialize` function again. This will trigger the authentication handler to fetch the new token.
    
    
    // Call this after successful authentication and the CCAI Platform Apps API update
    UJET.initialize({
      // ...include your existing parameters
      handlers: {
        authentication(callback) {
          // Fetch the new JWT for the newly authenticated user
          $.ajax({
            type: 'POST',
            url: 'https://your.company.com/api/ujet/sign',
            data: JSON.stringify({
              payload: {
                identifier: 'AUTHENTICATED-USER-UUID',
                name: 'Authenticated User Name'
              }
            }),
            success: function(result) {
              callback({
                token: result.token,
                user: {
                  identifier: 'AUTHENTICATED-USER-UUID',
                  name: 'Authenticated User Name'
                }
              });
            }
          });
        }
      }
    }).then(function() {
      // SDK successfully reinitialized with the authenticated user
    }).catch(function(error) {
      // Handle reinitialization errors
    });
    

**Why is this necessary?**

  * It ensures all subsequent actions, routing, and history are securely associated with the authenticated user, rather than an anonymous guest session.

  * It prevents data leakage and maintains accurate CRM and user records.




### Summary table

Scenario | Action required  
---|---  
User starts authenticated | Initialize SDK with the user's true UUID and JWT.  
User starts unauthenticated | Initialize SDK with a guest/random identifier.  
User authenticates mid-session | Update CCAI Platform with the API, generate a new JWT, and reinitialize the SDK.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
