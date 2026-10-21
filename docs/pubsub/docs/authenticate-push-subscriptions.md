---
url: https://docs.cloud.google.com/pubsub/docs/authenticate-push-subscriptions/
title: Authentication for push subscriptions \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:46:07.179384+00:00
---

# Authentication for push subscriptions  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/authenticate-push-subscriptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Authentication for push subscriptions Stay organized with collections  Save and categorize content based on your preferences. 

If a push subscription uses authentication, the Pub/Sub service signs a JSON Web Token (JWT) and sends the JWT in the authorization header of the push request. The JWT includes claims and a signature.

Subscribers can validate the JWT and verify the following:

  * The claims are accurate.
  * The Pub/Sub service signed the claims.



If subscribers use a firewall, they can't receive push requests. To receive push requests, you must turn off the firewall and verify the JWT. If a subscriber has a firewall, you might receive a `403 permission denied` error.

## Before you begin

  * Learn about [subscriptions](https://docs.cloud.google.com/pubsub/docs/subscription-overview).
  * Understand how [push subscriptions](https://docs.cloud.google.com/pubsub/docs/push) work.
  * [Create a push subscription](https://docs.cloud.google.com/pubsub/docs/create-push-subscription).



## JWT format

The JWT is an [OpenIDConnect JWT](https://openid.net/specs/draft-jones-json-web-token-07.html) that consists of a header, claim set, and signature. The Pub/Sub service encodes the JWT as a base64 string with period delimiters.

For example, the following authorization header includes an encoded JWT:
    
    
    "Authorization" : "Bearer
    eyJhbGciOiJSUzI1NiIsImtpZCI6IjdkNjgwZDhjNzBkNDRlOTQ3MTMzY2JkNDk5ZWJjMWE2MWMzZDVh
    YmMiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJodHRwczovL2V4YW1wbGUuY29tIiwiYXpwIjoiMTEzNzc0M
    jY0NDYzMDM4MzIxOTY0IiwiZW1haWwiOiJnYWUtZ2NwQGFwcHNwb3QuZ3NlcnZpY2VhY2NvdW50LmNvb
    SIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJleHAiOjE1NTAxODU5MzUsImlhdCI6MTU1MDE4MjMzNSwia
    XNzIjoiaHR0cHM6Ly9hY2NvdW50cy5nb29nbGUuY29tIiwic3ViIjoiMTEzNzc0MjY0NDYzMDM4MzIxO
    TY0In0.QVjyqpmadTyDZmlX2u3jWd1kJ68YkdwsRZDo-QxSPbxjug4ucLBwAs2QePrcgZ6hhkvdc4UHY
    4YF3fz9g7XHULNVIzX5xh02qXEH8dK6PgGndIWcZQzjSYfgO-q-R2oo2hNM5HBBsQN4ARtGK_acG-NGG
    WM3CQfahbEjZPAJe_B8M7HfIu_G5jOLZCw2EUcGo8BvEwGcLWB2WqEgRM0-xt5-UPzoa3-FpSPG7DHk7
    z9zRUeq6eB__ldb-2o4RciJmjVwHgnYqn3VvlX9oVKEgXpNFhKuYA-mWh5o7BCwhujSMmFoBOh6mbIXF
    cyf5UiVqKjpqEbqPGo_AvKvIQ9VTQ" 

The header and claim set are JSON strings. Once decoded, they take the following form:
    
    
    {"alg":"RS256","kid":"7d680d8c70d44e947133cbd499ebc1a61c3d5abc","typ":"JWT"}
    
    {
       "aud":"https://example.com",
       "azp":"113774264463038321964",
       "email":"gae-gcp@appspot.gserviceaccount.com",
       "sub":"113774264463038321964",
       "email_verified":true,
       "exp":1550185935,
       "iat":1550182335,
       "iss":"https://accounts.google.com"
      }

The tokens attached to requests sent to push endpoints may be up to an hour old.

## Configure Pub/Sub for push authentication

The following example shows how to set the push auth service account to a service account of your choice and how to grant the `iam.serviceAccountTokenCreator` role to the `service-{PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com` [service agent](https://docs.cloud.google.com/iam/docs/service-agents).

### Console

  1. Go to the **Pub/Sub Subscriptions** page.

[Go to the Subscriptions page](https://console.cloud.google.com/cloudpubsub/subscription)

  2. Click **Create subscription**.

  3. In the **Subscription ID** field, enter a name.

  4. Select a topic.

  5. Select **Push** as the **Delivery type**.

  6. Enter an endpoint URL.

  7. Check **Enable authentication**.

  8. Select a service account.

  9. Ensure that the service agent `service-{PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com` has the `iam.serviceAccountTokenCreator` role in your project's [IAM dashboard](https://console.cloud.google.com/iam-admin/iam). If the service account has not been granted the role, then click **Grant** in the IAM dashboard to do so.

  10. Optional: Enter an audience.

  11. Click **Create**.




### gcloud
    
    
    # Configure the push subscription
    gcloud pubsub subscriptions (create|update|modify-push-config) ${SUBSCRIPTION} \
     --topic=${TOPIC} \
     --push-endpoint=${PUSH_ENDPOINT_URI} \
     --push-auth-service-account=${SERVICE_ACCOUNT_EMAIL} \
     --push-auth-token-audience=${OPTIONAL_AUDIENCE_OVERRIDE}
    
    # Your service agent
    # `service-{PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com` needs to have the
    # `iam.serviceAccountTokenCreator` role.
    PUBSUB_SERVICE_ACCOUNT="service-${PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com"
    gcloud projects add-iam-policy-binding ${PROJECT_ID} \
     --member="serviceAccount:${PUBSUB_SERVICE_ACCOUNT}"\
     --role='roles/iam.serviceAccountTokenCreator'

When you're enabling authentication for a push subscription, you might encounter a `permission denied` or `not authorized` error. To resolve this issue, give the principal initiating the creation or update of the subscription the `iam.serviceAccounts.actAs` permission on the service account. For more information, see [Authentication](https://docs.cloud.google.com/pubsub/docs/create-push-subscription#authentication) in "Create push subscriptions."

If you use an authenticated push subscription with an App Engine application that is secured with [Identity-Aware Proxy](https://docs.cloud.google.com/iap/docs/concepts-overview), you must provide the IAP Client ID as your push auth token audience. To enable IAP on your App Engine application, see [Enabling IAP](https://docs.cloud.google.com/iap/docs/authenticate-users-google-accounts#enabling_iap). To find the IAP client ID, look for `IAP-App-Engine-app` Client ID on the [Credentials](https://console.cloud.google.com/apis/credentials) page.

### Claims

The JWT can be used to validate that the claims -- including `email` and `aud` claims -- are signed by Google. For more information about how Google's OAuth 2.0 APIs can be used for both authentication and authorization, see [OpenID Connect](https://developers.google.com/identity/protocols/OpenIDConnect).

There are two mechanisms that make these claims meaningful. First, Pub/Sub requires that the user or service account making the CreateSubscription, UpdateSubscription, or ModifyPushConfig call to have a role with the `iam.serviceAccounts.actAs` permission on the push auth service account. An example of such a role is the [`roles/iam.serviceAccountUser`](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) role.

Second, access to the certificates used to sign the tokens is tightly controlled. To create the token, Pub/Sub must call an internal Google service using a separate signing service account identity, which is the service agent `service-${PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com`. This signing service account must have the `iam.serviceAccounts.getOpenIdToken` permission or a **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`) on the push auth service account (or on any ancestor resource, such as the project, of the push auth service account).

### Validate tokens

Validating tokens sent by Pub/Sub to the push endpoint involves:

  * Checking the token integrity by using signature validation.
  * Ensuring that the _email_ and _audience_ claims in the token match the values set in the push subscription configuration.



The following example illustrates how to authenticate a push request to an App Engine application not secured with [Identity-Aware Proxy](https://docs.cloud.google.com/iap/docs/concepts-overview). If your App Engine application is secured with IAP, the HTTP request header that contains the IAP JWT is [`x-goog-iap-jwt-assertion`](https://docs.cloud.google.com/iap/docs/signed-headers-howto#securing_iap_headers) and must be [validated](https://docs.cloud.google.com/iap/docs/signed-headers-howto#retrieving_the_user_identity) accordingly.

### protocol

Request:
    
    
    GET https://oauth2.googleapis.com/tokeninfo?id_token={BEARER_TOKEN}
    

Response:
    
    
    200 OK
    
    
    {
        "alg": "RS256",
        "aud": "example.com",
        "azp": "104176025330667568672",
        "email": "{SERVICE_ACCOUNT_NAME}@{YOUR_PROJECT_NAME}.iam.gserviceaccount.com",
        "email_verified": "true",
        "exp": "1555463097",
        "iat": "1555459497",
        "iss": "https://accounts.google.com",
        "kid": "3782d3f0bc89008d9d2c01730f765cfb19d3b70e",
        "sub": "104176025330667568672",
        "typ": "JWT"
    }

### C#

Before trying this sample, follow the C# setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 
    
    
    /// <summary>
    /// Extended JWT payload to match the pubsub payload format.
    /// </summary>
    public class PubSubPayload : JsonWebSignature.Payload
    {
        [JsonProperty("email")]
        public string Email { get; set; }
        [JsonProperty("email_verified")]
        public string EmailVerified { get; set; }
    }
    /// <summary>
    /// Handle authenticated push request coming from pubsub.
    /// See the full sample in https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/main/appengine/flexible/Pubsub/Pubsub.Sample/Controllers/HomeController.cs
    /// </summary>
    [HttpPost]
    [Route("/AuthPush")]
    public async Task<IActionResult> AuthPushAsync([FromBody] PushBody body, [FromQuery] string token)
    {
        // Get the Cloud Pub/Sub-generated "Authorization" header.
        string authorizaionHeader = HttpContext.Request.Headers["Authorization"];
        string verificationToken = token ?? body.message.attributes["token"];
        // JWT token comes in `Bearer <JWT>` format substring 7 specifies the position of first JWT char.
        string authToken = authorizaionHeader.StartsWith("Bearer ") ? authorizaionHeader.Substring(7) : null;
        if (verificationToken != _options.VerificationToken || authToken is null)
        {
            return new BadRequestResult();
        }
        // Verify and decode the JWT.
        // Note: For high volume push requests, it would save some network
        // overhead if you verify the tokens offline by decoding them using
        // Google's Public Cert; caching already seen tokens works best when
        // a large volume of messages have prompted a single push server to
        // handle them, in which case they would all share the same token for
        // a limited time window.
        var payload = await JsonWebSignature.VerifySignedTokenAsync<PubSubPayload>(authToken);
    
        // IMPORTANT: you should validate payload details not covered
        // by signature and audience verification above, including:
        //   - Ensure that `payload.Email` is equal to the expected service
        //     account set up in the push subscription settings.
        //   - Ensure that `payload.Email_verified` is set to true.
    
        var messageBytes = Convert.FromBase64String(body.message.data);
        string message = System.Text.Encoding.UTF8.GetString(messageBytes);
        s_authenticatedMessages.Add(message);
        return new OkResult();
    }
    

### Go
    
    
    // receiveMessagesHandler validates authentication token and caches the Pub/Sub
    // message received.
    func (a *app) receiveMessagesHandler(w http.ResponseWriter, r *http.Request) {
    	if r.Method != "POST" {
    		http.Error(w, http.StatusText(http.StatusMethodNotAllowed), http.StatusMethodNotAllowed)
    		return
    	}
    
    	// Verify that the request originates from the application.
    	// a.pubsubVerificationToken = os.Getenv("PUBSUB_VERIFICATION_TOKEN")
    	if token, ok := r.URL.Query()["token"]; !ok || len(token) != 1 || token[0] != a.pubsubVerificationToken {
    		http.Error(w, "Bad token", http.StatusBadRequest)
    		return
    	}
    
    	// Get the Cloud Pub/Sub-generated JWT in the "Authorization" header.
    	authHeader := r.Header.Get("Authorization")
    	if authHeader == "" || len(strings.Split(authHeader, " ")) != 2 {
    		http.Error(w, "Missing Authorization header", http.StatusBadRequest)
    		return
    	}
    	token := strings.Split(authHeader, " ")[1]
    	// Verify and decode the JWT.
    	// If you don't need to control the HTTP client used you can use the
    	// convenience method idtoken.Validate instead of creating a Validator.
    	v, err := idtoken.NewValidator(r.Context(), option.WithHTTPClient(a.defaultHTTPClient))
    	if err != nil {
    		http.Error(w, "Unable to create Validator", http.StatusBadRequest)
    		return
    	}
    	// Please change http://example.com to match with the value you are
    	// providing while creating the subscription.
    	payload, err := v.Validate(r.Context(), token, "http://example.com")
    	if err != nil {
    		http.Error(w, fmt.Sprintf("Invalid Token: %v", err), http.StatusBadRequest)
    		return
    	}
    	if payload.Issuer != "accounts.google.com" && payload.Issuer != "https://accounts.google.com" {
    		http.Error(w, "Wrong Issuer", http.StatusBadRequest)
    		return
    	}
    
    	// IMPORTANT: you should validate claim details not covered by signature
    	// and audience verification above, including:
    	//   - Ensure that `payload.Claims["email"]` is equal to the expected service
    	//     account set up in the push subscription settings.
    	//   - Ensure that `payload.Claims["email_verified"]` is set to true.
    	if payload.Claims["email"] != "test-service-account-email@example.com" || payload.Claims["email_verified"] != true {
    		http.Error(w, "Unexpected email identity", http.StatusBadRequest)
    		return
    	}
    
    	var pr pushRequest
    	if err := json.NewDecoder(r.Body).Decode(&pr); err != nil {
    		http.Error(w, fmt.Sprintf("Could not decode body: %v", err), http.StatusBadRequest)
    		return
    	}
    
    	a.messagesMu.Lock()
    	defer a.messagesMu.Unlock()
    	// Limit to ten.
    	a.messages = append(a.messages, pr.Message.Data)
    	if len(a.messages) > maxMessages {
    		a.messages = a.messages[len(a.messages)-maxMessages:]
    	}
    
    	fmt.Fprint(w, "OK")
    }
    

### Java
    
    
    @WebServlet(value = "/pubsub/authenticated-push")
    public class PubSubAuthenticatedPush extends HttpServlet {
      private final String pubsubVerificationToken = System.getenv("PUBSUB_VERIFICATION_TOKEN");
      private final MessageRepository messageRepository;
      private final GoogleIdTokenVerifier verifier =
          new GoogleIdTokenVerifier.Builder(new NetHttpTransport(), new GsonFactory())
              /**
               * Please change example.com to match with value you are providing while creating
               * subscription as provided in @see <a
               * href="https://github.com/GoogleCloudPlatform/java-docs-samples/tree/main/appengine-java8/pubsub">README</a>.
               */
              .setAudience(Collections.singletonList("example.com"))
              .build();
      private final Gson gson = new Gson();
    
      @Override
      public void doPost(HttpServletRequest req, HttpServletResponse resp)
          throws IOException, ServletException {
    
        // Verify that the request originates from the application.
        if (req.getParameter("token").compareTo(pubsubVerificationToken) != 0) {
          resp.setStatus(HttpServletResponse.SC_BAD_REQUEST);
          return;
        }
        // Get the Cloud Pub/Sub-generated JWT in the "Authorization" header.
        String authorizationHeader = req.getHeader("Authorization");
        if (authorizationHeader == null
            || authorizationHeader.isEmpty()
            || authorizationHeader.split(" ").length != 2) {
          resp.setStatus(HttpServletResponse.SC_BAD_REQUEST);
          return;
        }
        String authorization = authorizationHeader.split(" ")[1];
    
        try {
          // Verify and decode the JWT.
          // Note: For high volume push requests, it would save some network overhead
          // if you verify the tokens offline by decoding them using Google's Public
          // Cert; caching already seen tokens works best when a large volume of
          // messsages have prompted a single push server to handle them, in which
          // case they would all share the same token for a limited time window.
          GoogleIdToken idToken = verifier.verify(authorization);
    
          GoogleIdToken.Payload payload = idToken.getPayload();
          // IMPORTANT: you should validate claim details not covered by signature
          // and audience verification above, including:
          //   - Ensure that `payload.getEmail()` is equal to the expected service
          //     account set up in the push subscription settings.
          //   - Ensure that `payload.getEmailVerified()` is set to true.
    
          messageRepository.saveToken(authorization);
          messageRepository.saveClaim(payload.toPrettyString());
          // parse message object from "message" field in the request body json
          // decode message data from base64
          Message message = getMessage(req);
          messageRepository.save(message);
          // 200, 201, 204, 102 status codes are interpreted as success by the Pub/Sub system
          resp.setStatus(102);
          super.doPost(req, resp);
        } catch (Exception e) {
          resp.setStatus(HttpServletResponse.SC_BAD_REQUEST);
        }
      }
    
      private Message getMessage(HttpServletRequest request) throws IOException {
        String requestBody = request.getReader().lines().collect(Collectors.joining("\n"));
        JsonElement jsonRoot = JsonParser.parseString(requestBody).getAsJsonObject();
        String messageStr = jsonRoot.getAsJsonObject().get("message").toString();
        Message message = gson.fromJson(messageStr, Message.class);
        // decode from base64
        String decoded = decode(message.getData());
        message.setData(decoded);
        return message;
      }
    
      private String decode(String data) {
        return new String(Base64.getDecoder().decode(data));
      }
    
      PubSubAuthenticatedPush(MessageRepository messageRepository) {
        this.messageRepository = messageRepository;
      }
    
      public PubSubAuthenticatedPush() {
        this(MessageRepositoryImpl.getInstance());
      }
    }

### Node.js
    
    
    app.post('/pubsub/authenticated-push', jsonBodyParser, async (req, res) => {
      // Verify that the request originates from the application.
      if (req.query.token !== PUBSUB_VERIFICATION_TOKEN) {
        res.status(400).send('Invalid request');
        return;
      }
    
      // Verify that the push request originates from Cloud Pub/Sub.
      try {
        // Get the Cloud Pub/Sub-generated JWT in the "Authorization" header.
        const bearer = req.header('Authorization');
        const [, token] = bearer.match(/Bearer (.*)/);
        tokens.push(token);
    
        // Verify and decode the JWT.
        // Note: For high volume push requests, it would save some network
        // overhead if you verify the tokens offline by decoding them using
        // Google's Public Cert; caching already seen tokens works best when
        // a large volume of messages have prompted a single push server to
        // handle them, in which case they would all share the same token for
        // a limited time window.
        const ticket = await authClient.verifyIdToken({
          idToken: token,
          audience: 'example.com',
        });
    
        const claim = ticket.getPayload();
    
        // IMPORTANT: you should validate claim details not covered
        // by signature and audience verification above, including:
        //   - Ensure that `claim.email` is equal to the expected service
        //     account set up in the push subscription settings.
        //   - Ensure that `claim.email_verified` is set to true.
    
        claims.push(claim);
      } catch (e) {
        res.status(400).send('Invalid token');
        return;
      }
    
      // The message is a unicode string encoded in base64.
      const message = Buffer.from(req.body.message.data, 'base64').toString(
        'utf-8'
      );
    
      messages.push(message);
    
      res.status(200).send();
    });

### Python
    
    
    @app.route("/push-handlers/receive_messages", methods=["POST"])
    def receive_messages_handler():
        # Verify that the request originates from the application.
        if request.args.get("token", "") != current_app.config["PUBSUB_VERIFICATION_TOKEN"]:
            return "Invalid request", 400
    
        # Verify that the push request originates from Cloud Pub/Sub.
        try:
            # Get the Cloud Pub/Sub-generated JWT in the "Authorization" header.
            bearer_token = request.headers.get("Authorization")
            token = bearer_token.split(" ")[1]
            TOKENS.append(token)
    
            # Verify and decode the JWT. `verify_oauth2_token` verifies
            # the JWT signature, the `aud` claim, and the `exp` claim.
            # Note: For high volume push requests, it would save some network
            # overhead if you verify the tokens offline by downloading Google's
            # Public Cert and decode them using the `google.auth.jwt` module;
            # caching already seen tokens works best when a large volume of
            # messages have prompted a single push server to handle them, in which
            # case they would all share the same token for a limited time window.
            claim = id_token.verify_oauth2_token(
                token, requests.Request(), audience="example.com"
            )
    
            # IMPORTANT: you should validate claim details not covered by signature
            # and audience verification above, including:
            #   - Ensure that `claim["email"]` is equal to the expected service
            #     account set up in the push subscription settings.
            #   - Ensure that `claim["email_verified"]` is set to true.
    
            CLAIMS.append(claim)
        except Exception as e:
            return f"Invalid token: {e}\n", 400
    
        envelope = json.loads(request.data.decode("utf-8"))
        payload = base64.b64decode(envelope["message"]["data"])
        MESSAGES.append(payload)
        # Returning any 2xx status indicates successful receipt of the message.
        return "OK", 200

### Ruby
    
    
    post "/pubsub/authenticated-push" do
      halt 400 if params[:token] != PUBSUB_VERIFICATION_TOKEN
    
      begin
        bearer = request.env["HTTP_AUTHORIZATION"]
        token = /Bearer (.*)/.match(bearer)[1]
        claim = Google::Auth::[IDTokens](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens.html).[verify_oidc](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens.html) token, aud: "example.com"
    
        # IMPORTANT: you should validate claim details not covered by signature
        # and audience verification above, including:
        #   - Ensure that `claim["email"]` is equal to the expected service
        #     account set up in the push subscription settings.
        #   - Ensure that `claim["email_verified"]` is set to true.
    
        claims.push claim
      rescue Google::Auth::[IDTokens](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens.html)::[VerificationError](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens-VerificationError.html) => e
        puts "VerificationError: #{e.message}"
        halt 400, "Invalid token"
      end
    
      message = JSON.parse request.body.read
      payload = Base64.decode64 message["message"]["data"]
    
      messages.push payload
    end

For information on the environment variable `PUBSUB_VERIFICATION_TOKEN` used in the code samples above, see [Writing and responding to Pub/Sub messages](https://docs.cloud.google.com/appengine/docs/flexible/python/writing-and-responding-to-pub-sub-messages).

Find additional examples of how to validate the bearer JWT in this [guide for Google Sign-in for websites](https://developers.google.com/identity/sign-in/web/backend-auth). A broader overview of OpenID tokens is available in the [OpenID Connect Guide](https://developers.google.com/identity/protocols/oauth2/openid-connect#validatinganidtoken), including a list of [client libraries](https://developers.google.com/identity/protocols/oauth2/openid-connect#libraries) that help validate JWTs.

## Authentication from other Google Cloud services

Cloud Run and App Engine functions authenticate HTTP calls from Pub/Sub by verifying Pub/Sub-generated tokens. The only configuration that you require is to grant the necessary IAM roles to the caller account.

See the following guides and tutorials for different use cases with these services:

### Cloud Run

  * [Triggering from Pub/Sub push](https://docs.cloud.google.com/run/docs/events/pubsub-push): Your push auth service account must have the [`roles/run.invoker`](https://docs.cloud.google.com/run/docs/reference/iam/roles#standard-roles) role and be bound to a Cloud Run service to invoke a corresponding Cloud Run service
  * [Using Pub/Sub with Cloud Run tutorial](https://docs.cloud.google.com/run/docs/tutorials/pubsub)



### App Engine

  * [Writing and Responding to Pub/Sub Messages](https://docs.cloud.google.com/appengine/docs/flexible/python/writing-and-responding-to-pub-sub-messages)

**Note:** If your App Engine application is secured with [Identity-Aware Proxy](https://docs.cloud.google.com/iap/docs/concepts-overview), you must grant your push auth service account the [IAP-secured Web App User](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.roles/iap.httpsResourceAccessor) role on the App Engine application for Pub/Sub push requests to come through. See [**Add access**](https://docs.cloud.google.com/iap/docs/managing-access#add_access) for a detailed guide.

### Cloud Run functions

  * [HTTP Triggers](https://docs.cloud.google.com/functions/docs/calling/http): Your push auth service account must have the [`roles/cloudfunctions.invoker`](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.invoker) role to invoke a function if you intend to use Pub/Sub push requests as HTTP triggers to the function
  * [Google Cloud Pub/Sub Triggers](https://docs.cloud.google.com/functions/docs/calling/pubsub): IAM roles and permissions are auto-configured if you use Pub/Sub triggers to invoke a function

**Note:** In [first-generation](https://docs.cloud.google.com/appengine/docs/standard/runtimes) App Engine runtimes, push requests to endpoint URLs of the form `/_ah/push-handlers/.*` in the same project are authorized as [ admin users](https://docs.cloud.google.com/appengine/docs/standard/python/users/adminusers). This ACL mechanism is no longer supported in [second generation](https://docs.cloud.google.com/appengine/docs/standard/runtimes) App Engine runtimes. In second-generation App Engine runtimes, grant IAM roles for admin use to the push auth service account that your push subscription is configured with. For more details, visit [ Authenticating Users](https://docs.cloud.google.com/appengine/docs/standard/python3/authenticating-users) and [ Understanding Access Control](https://docs.cloud.google.com/appengine/docs/standard/python3/access-control). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
