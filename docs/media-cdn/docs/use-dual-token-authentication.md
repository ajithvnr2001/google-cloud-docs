---
url: https://docs.cloud.google.com/media-cdn/docs/use-dual-token-authentication/
title: Use dual-token authentication \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:52.135722+00:00
---

# Use dual-token authentication  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/use-dual-token-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Use dual-token authentication Stay organized with collections  Save and categorize content based on your preferences. 

To enforce dual-token authentication when viewers access a streaming resource, you configure separate _routes_. A route is a configuration that matches requests for Media CDN and directs HTTP traffic to an origin. Media CDN supports routes for either HTTP live streaming (HLS) or Dynamic Adaptive Streaming over HTTP (DASH) resources. For more information about routes in Media CDN, see [Configure service routes](https://docs.cloud.google.com/media-cdn/docs/routing).

For HLS streams, Media CDN supports dual-token authentication through cookies and URL query parameters (cookieless). For DASH streams, Media CDN supports only cookie-based dual-token authentication.

This page describes how to configure Media CDN routes to help protect content by using dual-token authentication.

## Before you begin

Do the following:

  1. For short-duration tokens, choose one of the following signature algorithms:

     * Ed25519 signatures
     * Symmetric-key hash-based message authentication codes (HMACs)

You can enable symmetric HMAC signing algorithms only for routes configured to generate new long-duration tokens. We recommend that you use Ed25519 signatures for optimal performance and security and symmetric-key HMACs only when necessary for compatibility with other CDNs.

  2. Include the required keys in an [`EdgeCacheKeyset` resource](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheKeysets).

Tokens must be signed or verified with keys in an `EdgeCacheKeyset` resource. The keyset must include the correct keys for the selected signature algorithm. The following table describes each of the signature algorithms and their required keys.

Signature algorithm | Required keys in the keyset  
---|---  
Ed25519 | Public keys  
HMAC-SHA1 | Validation shared keys  
HMAC-SHA256 | Validation shared keys  
  
As a best practice, make two separate keysets, one for short-duration tokens and another for long-duration tokens.

However, if you're using DASH and dynamic media presentation description (MPD) files, you must use the same keyset for both long-duration and short-duration tokens.

  3. For long-duration tokens, choose one of the following token formats:

     * Cookies
     * URL query parameters



### Set up short-duration tokens

Depending on the signature algorithm that you want to use, set up short-duration tokens by using one of the following options.

###  Ed25519 signature 

  1. Generate a private key:
         
         openssl genpkey -algorithm ed25519 -outform PEM -out SSL_KEY_NAME.private.key
         

Replace `SSL_KEY_NAME` with a key name.

  2. Generate a public key from the private key:
         
         openssl pkey -outform DER -pubout -in SSL_KEY_NAME.private.key |\
         tail -c +13 |\
         python3 -c "import base64, sys; print(('%s' % base64.urlsafe_b64encode(sys.stdin.buffer.read()))[2:-1])"
         

  3. Create a new keyset with a single public key:

###  Console 

     1. In the Google Cloud console, go to the **Media CDN** page.

[Go to Media CDN](https://console.cloud.google.com/net-services/media-cdn)

     2. Click the **Keysets** tab.

     3. Click add**Create keyset**.

     4. For **Name** , enter a unique keyset name.

     5. Optional: For **Description** , enter a description for your keyset.

     6. Optional: Click **Add label** , and then enter one or more key-value pairs for your keyset.

     7. Click **Add public key** , and then do the following:

        1. For **ID** , enter an alphanumeric ID.
        2. Select **Enter the value** , and then specify the base64-encoded value of your Ed25519 public key.
     8. Click **Create keyset**.

###  gcloud 

Use the [`gcloud edge-cache keysets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/create).
    
    gcloud edge-cache keysets create SHORT_KEYSET_NAME \
      --public-key='id=SSL_PUBLIC_KEY_NAME,value=SSL_PUBLIC_KEY_VALUE'
    

Replace the following:

     * `SHORT_KEYSET_NAME`: a unique keyset name—for example, `prod-vod-keyset`
     * `SSL_PUBLIC_KEY_NAME`: the name of your SSL public key
     * `SSL_PUBLIC_KEY_VALUE`: the value of your SSL public key

To review the keys associated with the keyset, use the [`gcloud edge-cache keysets describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/describe).
    
    gcloud edge-cache keysets describe prod-vod-keyset
    

The output is similar to the following:
    
    name: prod-vod-keyset
    description: "Keyset for prod.example.com"
    publicKeys:
    - id: "key-20200918"
      value: "DThVLjhAKm3VYOvLBAwFZ5XbjVyF98Ias8NZU0WEM9w"
    - id: "key-20200808"
      value: "Lw7LDSaDUrbDdqpPA6JEmMF5BA5GPtd7sAjvsnh7uDA="
    

###  Terraform 
    
    resource "google_network_services_edge_cache_keyset" "default" {
      name        = "prod-vod-keyset"
      description = "Keyset for prod.example.com"
      public_key {
        id    = "key-20200918"
        value = "FHsTyFHNmvNpw4o7-rp-M1yqMyBF8vXSBRkZtkQ0RKY" # Update Ed25519 public key
      }
      public_key {
        id    = "key-20200808"
        value = "Lw7LDSaDUrbDdqpPA6JEmMF5BA5GPtd7sAjvsnh7uDA=" # Update Ed25519 public key
      }
    }




###  Symmetric-key HMAC 

  1. If you haven't used Secret Manager before, [configure Secret Manager](https://docs.cloud.google.com/secret-manager/docs/configuring-secret-manager).

  2. [Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#create).

  3. [Add a secret version](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#add-secret-version) in binary format.

  4. Grant the [Secret Manager Access role](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager) (`roles/secretmanager.secretAccessor`) to the Media CDN service account:

###  Console 

     1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

     2. Select the checkbox next to the name of the secret.

     3. Click **Show Info Panel**.

     4. In the info panel, click **Add principal**.

     5. For **New principals** , enter the Media CDN service account in this format:
            
            service-PROJECT_NUMBER@gcp-sa-mediaedgefill.iam.gserviceaccount.com
            

Replace `PROJECT_NUMBER` with your project number.

     6. For **Select a role** , select **Secret Manager** , and then select **Secret Manager Secret Accessor**.

###  gcloud 

[Use the `gcloud secrets add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/secrets/add-iam-policy-binding).
    
    gcloud secrets add-iam-policy-binding projects/PROJECT_NUMBER/secrets/SECRET_ID \
      --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-mediaedgefill.iam.gserviceaccount.com" \
      --role="roles/secretmanager.secretAccessor"
    

Replace the following:

     * `PROJECT_NUMBER`: your project number
     * `SECRET_ID`: the ID of the secret

  5. [Access your secret versions](https://docs.cloud.google.com/secret-manager/docs/access-secret-version#access_a_secret_version) and copy the secret paths, including version numbers.

  6. Create a new keyset with the shared secrets in a validation shared key:

###  Console 

     1. In the Google Cloud console, go to the **Media CDN** page.

[Go to Media CDN](https://console.cloud.google.com/net-services/media-cdn)

     2. Click the **Keysets** tab.

     3. Click add**Create keyset**.

     4. For **Name** , enter a unique keyset name.

     5. Optional: For **Description** , enter a description for your keyset.

     6. Optional: Click **Add label** , and then enter one or more key-value pairs for your keyset.

     7. To specify a validation shared key, click **Add validation shared key** , and then do the following:

        1. For **Secret** , select a secret from the list, enter a secret manually by specifying its resource ID, or [create a new secret](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart#create_a_secret_and_access_a_secret_version) and then select it.

        2. For **Secret version** , select a version from the list or [create a new secret version](https://docs.cloud.google.com/secret-manager/docs/add-secret-version#add-secret-version) and then select it.

     8. Click **Create keyset**.

###  gcloud 

Use the [`gcloud edge-cache keysets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/create).
    
    gcloud edge-cache keysets create SHORT_KEYSET_NAME \
      --validation-shared-key='secret_version=projects/PROJECT_NUMBER/secrets/SECRET_ID/versions/KEY_VERSION'
    

Replace the following:

     * `SHORT_KEYSET_NAME`: a unique name for the keyset—for example, `prod-vod-keyset`
     * `PROJECT_NUMBER`: your project ID
     * `SECRET_ID`: the resource ID of the secret
     * `KEY_VERSION`: the secret version that you want to use




### Set up long-duration tokens

Google-owned and managed keys are scoped by keyset. That means that two different keysets have different Google-owned and managed keys. Google-owned and managed keys are rotated regularly.

Set up long-duration tokens by using one of the following options:

###  Console 

  1. [Create or modify a keyset](https://docs.cloud.google.com/media-cdn/docs/create-keyset#create-keyset).

  2. In the **Keys** section, select **Use Google-owned and managed key for dual-token authentication**.




###  gcloud and YAML 

Use either of the following options:

  * Create a Google-managed signing key:
        
        gcloud edge-cache keysets create LONG_KEYSET_NAME \
            --public-key='id=google-managed-key,managed=true'
        

Replace `LONG_KEYSET_NAME` with a key name—for example, `prod-vod-keyset-long`.

  * Modify an existing keyset:

    1. Export your keyset to a YAML file. Use the [`gcloud edge-cache keysets export` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/export).
           
           gcloud edge-cache keysets export LONG_KEYSET_NAME \
              --destination=prod-vod-keyset-long.yaml
           

    2. In a text editor or in your configuration management tooling, edit your keyset configuration so that it looks similar to the following:
           
           name: projects/my-project/locations/global/edgeCacheKeysets/LONG_KEYSET_NAME
           publicKeys:
           - id: some-key
             value: MC4CAQAwBQYDK2VwBCIEINV2iYugIWBuvGBJUQ_Ab69E4v4zcVqvgYHw-iZxGzcd
           - id: google-managed-key
             managed: true
           

    3. Import the edited keyset. Use the [`gcloud edge-cache keysets import` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/import):
           
           gcloud edge-cache keysets import LONG_KEYSET_NAME \
               --source=prod-vod-keyset-long.yaml
           




You can include additional public keys in the long-duration token keyset. The keyset may have at most three public keys. In practice, this means that the keyset can have two user-managed keys and one Google-owned and managed key.

Media CDN always uses the Google-owned and managed key to generate tokens. The user-managed keys can be used only for verification.

Including additional public keys is useful to let your player application access media playlists and media segments by using signed requests that are generated by your own private keys.

## Configure token exchange

This section shows how to configure token exchange by creating multiple routes. A route lets you optimize behavior based on the type of content, client attributes, and your freshness requirements. In the following examples, we use routes to configure token exchange for each part of a media request.

### Configure the primary manifest route to require short-duration tokens

Configure Media CDN to require short-duration tokens on the primary manifest route.

### Console

Enable short-duration token authentication on the primary manifest route:

  1. In the Google Cloud console, go to the **Media CDN** page.

[Go to Media CDN](https://console.cloud.google.com/net-services/media-cdn)

  2. To open the **Details** page of a service, click the service name.

  3. To switch to the edit mode, click the **Edit** button.

  4. To navigate to the **Routing** section, click **Next**.

  5. Expand the host rule to which you'd like to add the primary manifest route rule.

  6. Click **Add route rule**.

Alternatively, to edit a route rule, click edit**Edit** on the respective row.

  7. In the **Edit route rule** pane, for **Priority** , set a value—for example, `1`.

  8. For **Description** , provide a brief description that can help identify the rule in the list of rules.

  9. In the **Match** section, click **Add a match condition**. Then, do the following:

     1. For **Match type** , select **Path template match**.
     2. For **Path match** , specify the names or path templates for the HLS primary playlist (M3U8) or DASH manifest (MPD) file. For more information, see [Path matching](https://docs.cloud.google.com/media-cdn/docs/routing#path-matching).
  10. Click **Advanced configurations**.

  11. In the **Route action** section, click **Add an item**.

  12. For **Type** , select **CDN policy**.

  13. In the **Signed request** section, for **Signed request mode** , select **Require tokens**.

  14. In the **Signed request keyset** section, do the following:

     1. To specify the keyset for short-duration tokens, click **Select a keyset** and select your [short-duration token keyset](https://docs.cloud.google.com/media-cdn/docs/use-dual-token-authentication#set-up-short-duration-tokens).

Alternatively, to create a new keyset that has the keys that you need, click **Create new keyset**. Then, select it.

     2. For **Signature algorithm** , select **Ed25519 using public keys**.

     3. For **Token query parameter** , retain the default value, `edge-cache-token`.

Alternatively, if you plan to use HLS manifest URL query parameters rather than cookies for authentication, specify the parameter in which to store the request tokens.

     4. For **Max time to live** , specify, in seconds, the maximum lifespan of incoming request tokens.

  15. To save the changes in the **Route action** section, click **Done**.

  16. To save the changes in the route rule, click **Save**.




###  gcloud and YAML 

  1. [Export your Media CDN configuration](https://docs.cloud.google.com/media-cdn/docs/configuration#import-and-export) into a YAML file. Use the [`gcloud edge-cache services export` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/services/export).
         
         gcloud edge-cache services export SERVICE_NAME \
             --destination=FILENAME.yaml
         

Replace the following:

     * `SERVICE_NAME`: the name of your service
     * `FILENAME` : the name of your YAML file
  2. To enable short-duration token authentication in the primary manifest route rule, in the route's `cdnPolicy` section of the YAML file, specify a `signedTokensOptions` configuration.
         
         pathMatchers:
           - name: "ROUTE_NAME"
             routeRules:
             - priority: 1
               description: "ROUTE_DESCRIPTION"
               origin: "ORIGIN_NAME"
               matchRules:
               - pathTemplateMatch: "/MANIFEST_OR_PLAYLIST"
               routeAction:
                 cdnPolicy:
                   cacheMode: CACHE_ALL_STATIC
                   signedRequestMode: REQUIRE_TOKENS
                   signedRequestKeyset: SHORT_KEYSET_NAME
                   signedRequestMaximumExpirationTtl: SIGNED_REQUEST_MAXIMUM_EXPIRATION_TIME
                   signedTokenOptions:
                     tokenQueryParameter: SHORT_TOKEN_NAME
         

Replace the following:

     * `ROUTE_NAME`: the name of the route rule
     * `ROUTE_DESCRIPTION`: a description of the route rule
     * `ORIGIN_NAME`: the origin name
     * `MANIFEST_OR_PLAYLIST`: the name of the HLS primary playlist (M3U8) or DASH manifest (MPD) file. For more information, see [Path matching](https://docs.cloud.google.com/media-cdn/docs/routing#path-matching).
     * `SHORT_KEYSET_NAME`: the keyset name to use for short-duration tokens
     * `SIGNED_REQUEST_MAXIMUM_EXPIRATION_TIME`: the expiration time for signed requests—for example, `600s`. For more information, see [`signedRequestMaximumExpirationTtl`](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices#CDNPolicy.FIELDS.signed_request_maximum_expiration_ttl).
     * Optional: `SHORT_TOKEN_NAME`: the query parameter in which to find the short token. The default value is `edge-cache-token`. For more information, see [`SignedTokenOptions`](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices#SignedTokenOptions.FIELDS.token_query_parameter).

When using symmetric-key HMACs, in the `signedTokenOptions` section, append `allowedSignatureAlgorithms` with its value as `HMAC_SHA_256`:
    
    allowedSignatureAlgorithms:
           - HMAC_SHA_256
    

  3. To update the service, [import your Media CDN configuration](https://docs.cloud.google.com/media-cdn/docs/configuration#import-and-export) from the YAML file. Use the [`gcloud edge-cache services import` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/services/import).
         
         gcloud edge-cache services import SERVICE_NAME \
             --source=FILENAME.yaml
         




This completes the process of enabling single-token authentication.

To configure dual-token authentication, proceed to the following sections.

### Configure the primary manifest route rule to generate long-duration tokens

Configure Media CDN to generate long-duration tokens on the primary manifest route. Choose either cookies or URL query parameters to generate these tokens.

### Console

Modify the primary manifest route rule so that Media CDN can generate long-duration tokens on the route:

  1. On the **Edit route rule** page, click **Advanced configurations**.
  2. For **Type** , select **CDN policy**.
  3. Expand **Dual-token authentication**.
  4. For **Signature action** , select **Generate new long-duration token**.
  5. For **Signature type** , select either of the following options:

     * **via cookies (for HLS and DASH streaming)** : configures Media CDN to return an `Edge-Cache-Cookie` with the primary manifest response.
     * **via HLS manifest URL query parameters (cookieless)** : configures Media CDN to manipulate the HLS primary manifest by appending a long-duration token to each URL.
  6. In the **Generate new long-duration token** section, do the following:

     1. To specify a keyset for long-duration tokens, click **Select a keyset** and select your [long-duration token keyset](https://docs.cloud.google.com/media-cdn/docs/use-dual-token-authentication#create-long-duration-keyset).

Alternatively, click **Create new keyset** to create a new keyset that has the keys that you need. Then, select it.

     2. For **Token TTL** , specify, in seconds, the maximum lifespan of the long-duration token.

     3. For **Signature type** , if you selected the **via cookies** option, then, in the **Copied parameters** section, select the parameters that you want Media CDN to copy from the short-duration token to the long-duration token. To use dual-token authentication, you must select either `PathGlobs` (or either of its aliases, `acl` or `paths`) or `URLPrefix`.

If you selected the **via HLS manifest URL query parameters** option, for **Token query parameter** , retain the default value, `edge-cache-token`.

  7. To save the changes in the **Route action** section, click **Done**.

  8. To save the changes in the route rule, click **Save**.

A message appears asking if you'd like to create the routes for media playlists and segments automatically or manually. If you select the automatic option, a single new route is created for the cookies signature and two routes for the cookieless signature. If you select the manual option, proceed to the next section.




###  gcloud and YAML 

Modify the `addSignatures` section of the primary manifest route rule so that Media CDN can generate long-duration tokens on the route:

###  Cookies 
    
    
              addSignatures:
                actions:
                  - GENERATE_COOKIE
                keyset: LONG_KEYSET_NAME
                tokenTtl: TOKEN_EXPIRATION_TIME
                copiedParameters:
                  - PathGlobs
                  - SessionID
    

Replace the following:

  * `LONG_KEYSET_NAME`: the name of your long-duration token keyset

  * `TOKEN_EXPIRATION_TIME`: the expiration time of the long-duration token—for example, `86400s` for a one-day expiration time




This code example implements the following changes:

  * `addSignatures.actions: GENERATE_COOKIE`: configures Media CDN to return an `Edge-Cache-Cookie` with the primary manifest response

  * `copiedParameters.PathGlobs`: configures Media CDN to copy the `PathGlobs` from the short-duration token to the long-duration token. To use dual-token authentication, you must use either `copiedParameters.PathGlobs` or `copiedParameters.URLPrefix`. For more information, see [`copiedParameters`](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices#AddSignaturesOptions.FIELDS.copied_parameters).

  * Optional: `copiedParameters.SessionID`: configures Media CDN to copy the `SessionID` from the short-duration token to the long-duration token




When the `GENERATE_COOKIE` action is applied, Media CDN returns a `Set-Cookie` header similar to the following with the primary manifest response:
    
    
    Set-Cookie: Edge-Cache-Cookie=PathGlobs=PATHS~SessionID=**SESSION_ID** ~Expires=EXPIRATION~_GO=Generated~Signature=**SIGNATURE**
    

###  URL query parameters 
    
    
              addSignatures:
                actions:
                  - GENERATE_TOKEN_HLS_COOKIELESS
                keyset: LONG_KEYSET_NAME
                tokenTtl: TOKEN_EXPIRATION_TIME
                copiedParameters:
                  - PathGlobs
                  - SessionID
                tokenQueryParameter: LONG_TOKEN_NAME
    

Replace the following:

  * `LONG_KEYSET_NAME`: the name of your long-duration keyset

  * `TOKEN_EXPIRATION_TIME`: the expiration time of the long-duration token—for example, `86400s` for a one-day expiration time




This code example implements the following changes:

  * `addSignatures.actions: GENERATE_TOKEN_HLS_COOKIELESS`: configures Media CDN to manipulate the HLS primary manifest by appending a long-duration token to each URI present.

  * `copiedParameters.PathGlobs`: configures Media CDN to copy the `PathGlobs` from the short-duration token to the long-duration token. To use dual-token authentication, you must use one of `copiedParameters.PathGlobs` or `copiedParameters.URLPrefix`. For more information, see [`copiedParameters`](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices#AddSignaturesOptions.FIELDS.copied_parameters).

  * Optional: `copiedParameters.SessionID`: configures Media CDN to copy the `SessionID` from the short-duration token to the long-duration token.

  * Optional: `LONG_TOKEN_NAME`: the query parameter in which to put the generated long token. The default value is `edge-cache-token`. For more information, see [`tokenQueryParameter`](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices#AddSignaturesOptions.FIELDS.token_query_parameter).




The following manifest file shows the `GENERATE_TOKEN_HLS_COOKIELESS` action applied:
    
    
    #EXTM3U
    #EXT-X-STREAM-INF:BANDWIDTH=1280000,AVERAGE-BANDWIDTH=1000000
    http://example.com/HLS_PRIMARY_PLAYLIST.m3u8?LONG_TOKEN_NAME=PathGlobs=PATHS~SessionID=**SESSION_ID** ~Expires=EXPIRATION~_GO=Generated~Signature=SIGNATURE
    

Media CDN verifies the short-duration token and then generates and stores the long-duration token in the `LONG_TOKEN_NAME` query parameter.

### Configure the media playlist and segments routes to require long-duration tokens

Configure the media playlist and segments routes to require long-duration tokens.

### Console

### Cookies

Create a route rule for the media playlist and segments route:

  1. On the **Edit Edge Cache service** page, in the **Routing** section, click the host rule that has the primary manifest route.
  2. Click **Add route rule**.
  3. In the **Edit route rule** pane, for **Priority** , set a value that's greater than that of the primary manifest route—for example, `2`. Higher values indicate lower priority.
  4. For **Description** , provide a brief description that can help identify the rule in the list of rules.
  5. Set the following fields as suggested:

     * **Select an origin** : same as for the primary manifest route rule
     * **Add a match condition** : same as for the primary manifest route rule
     * **Type** : **CDN policy**
     * **Signed request mode** : **Require tokens**
     * **Select a keyset** : same as for long-duration tokens
     * **Signature algorithm** : same as for the primary manifest route rule
  6. Expand **Dual-token authentication**.

  7. For **Signature action** , retain the default value **None**.

  8. Click **Done** , and then click **Save**.




### URL query parameters

  1. Create a route rule for the media playlist.

     1. On the **Edit Edge Cache service** page, in the **Routing** section, click the host rule that has the primary manifest route.
     2. Click **Add route rule**.
     3. In the **Edit route rule** pane, for **Priority** , set a value that's greater than that of the primary manifest route—for example, `2`. Higher values indicate lower priority.
     4. For **Description** , provide a brief description that can help identify the rule in the list of rules.
     5. Set the following fields as suggested:

        * **Select an origin** : the same as for the primary manifest route rule
        * **Add a match condition** : the same as for the primary manifest route rule
        * **Type** : **CDN policy**
        * **Signed request mode** : **Require tokens**
        * **Select a keyset** : the same as for long-duration tokens
        * **Signature algorithm** : the same as for the primary manifest route rule
        * **Token query parameter** : the same as for long-duration tokens
     6. Expand **Dual-token authentication**.

     7. For **Signature action** , select **Propagate existing long-duration token**.

This option is enabled only after Media CDN verifies that the long-duration token was generated by using the **via HLS manifest URL query parameters (cookieless)** signature type.

     8. For **Token query parameter** , retain the default value, `edge-cache-token`.

     9. Click **Done** , and then click **Save**.

  2. Create a route rule for media segments.

This route is like the route for media playlists, with the following key differences:

     * For **Priority** , set a value that's greater than that of the media playlist route rule—for example, `3`.
     * For **Description** , provide a brief description that can help identify the rule in the list of rules.
     * In the **Dual-token authentication** section, for **Signature action** , retain the default value **None**.



###  gcloud and YAML 

Edit the YAML file:

### Cookies

Configure the media playlist and segments to require long-duration cookies:
    
    
        - priority: 2
          description: "SEGMENTS_ROUTE_DESCRIPTION"
          origin: "ORIGIN_NAME"
          matchRules:
          - pathTemplateMatch: "/**.m3u8" # HLS media playlists
          - pathTemplateMatch: "/**.ts" # HLS segments
          - pathTemplateMatch: "/**.m4s" # DASH / CMAF segments
          routeAction:
            cdnPolicy:
              cacheMode: CACHE_ALL_STATIC
              signedRequestMode: REQUIRE_TOKENS
              signedRequestKeyset: LONG_KEYSET_NAME
    

Replace SEGMENTS_ROUTE_DESCRIPTION with a description of the route.

This code example implements the following changes:

  * `priority: 2`: the priority of the route. Higher values indicate lower priority. Because the route for your media playlists and media segments matches any filename ending in `.m3u8`, the priority for the route must be lower than the route you previously created for the primary manifest.
  * `signedRequestMode: REQUIRE_TOKENS`: enforces tokens for media playlists and media segments. If you're using static media presentation description (MPD) files, then the long and short keysets may be different. If you're using dynamic MPD files, then the long and short keysets must be the same.
  * `signedRequestKeyset: LONG_KEYSET_NAME`: Media CDN uses the long-duration keyset to validate the long-duration cookie supplied by a user agent for media playlist and media segment requests.



### URL query parameters

Add two route configurations:

  1. Configure the HLS media manifest routes to propagate long-duration tokens:
         
         - priority: 2
              description: "PLAYLIST_ROUTE_DESCRIPTION"
              origin: "ORIGIN_NAME"
              matchRules:
              - pathTemplateMatch: "/**.m3u8" # HLS media playlists
              routeAction:
                cdnPolicy:
                cacheMode: CACHE_ALL_STATIC
                signedRequestMode: REQUIRE_TOKENS
                signedRequestKeyset: LONG_KEYSET_NAME
                addSignatures:
                  actions:
                  - PROPAGATE_TOKEN_HLS_COOKIELESS
         

Replace PLAYLIST_ROUTE_DESCRIPTION with a description of the route.

This code example implements the following changes:

     * `priority: 2`: the priority of the route. Higher values indicate lower priority. Because the route for your media playlists matches any filename ending in `.m3u8`, the priority for the route must be lower than the route you previously created for the primary manifest.
     * `signedRequestMode: REQUIRE_TOKENS`: enforces tokens for media playlists and media segments. If you're using static media presentation description (MPD) files, the long and short keysets may be different. If you're using dynamic MPD files, then the long and short keysets must be the same.
     * `signedRequestKeyset: LONG_KEYSET_NAME`: Media CDN uses the long-duration keyset to validate the long-duration cookie supplied by a user agent for media playlist and media segment requests.
     * `addSignatures.actions: PROPAGATE_TOKEN_HLS_COOKIELESS`: configures Media CDN to copy the long-duration token to media segment URIs in the media playlists.
  2. Configure the segment routes to require long-duration tokens:
         
         - priority: 3
              description: "SEGMENTS_ROUTE_DESCRIPTION"
              origin: "ORIGIN_NAME"
              matchRules:
              - pathTemplateMatch: "/**.ts" # HLS segments
              routeAction:
                cdnPolicy:
                  cacheMode: CACHE_ALL_STATIC
                  signedRequestMode: REQUIRE_TOKENS
                  signedRequestKeyset: LONG_KEYSET_NAME
         

Replace SEGMENTS_ROUTE_DESCRIPTION with a description of the route.

This code example implements the following changes:

     * `priority: 3`: the priority of the route. Higher values indicate lower priority. The priority for this route must be lower than the route you previously created for the media playlists.
     * `signedRequestMode: REQUIRE_TOKENS`: enforces tokens for media playlists and media segments.
     * `signedRequestKeyset: LONG_KEYSET_NAME`: Media CDN uses the long-duration keyset to validate the long-duration signed token supplied by a user agent for media playlist and media segment requests.



### Example configuration file

The following code sample shows a completed configuration file:

###  Cookies 
    
    
    name: SERVICE_NAME
    routing:
      hostRules:
      - hosts:
        - DOMAIN_NAME
        pathMatcher: routes
      pathMatchers:
        - name: "ROUTE_NAME"
          routeRules:
          - priority: 1
            description: "ROUTE_DESCRIPTION"
            origin: "ORIGIN_NAME"
            matchRules:
            - pathTemplateMatch: "/HLS_MASTER_PLAYLIST.m3u8" # HLS primary playlists
            - pathTemplateMatch: "/DASH_MANIFESTS.mpd" # DASH manifests
            routeAction:
              cdnPolicy:
                cacheMode: CACHE_ALL_STATIC
                signedRequestMode: REQUIRE_TOKENS
                signedRequestKeyset: SHORT_KEYSET_NAME
                signedRequestMaximumExpirationTtl: SIGNED_REQUEST_MAXIMUM_EXPIRATION_TIME
                addSignatures:
                  actions:
                    - GENERATE_COOKIE
                  keyset: LONG_KEYSET_NAME
                  tokenTtl: TOKEN_EXPIRATION_TIME
                  copiedParameters:
                    - PathGlobs
                    - SessionID
          - priority: 2
            description: "SEGMENTS_ROUTE_DESCRIPTION"
            origin: "ORIGN_NAME"
            matchRules:
            - pathTemplateMatch: "/**.m3u8" # HLS media playlists
            - pathTemplateMatch: "/**.ts" # HLS segments
            - pathTemplateMatch: "/**.m4s" # DASH / CMAF segments
            routeAction:
              cdnPolicy:
                cacheMode: CACHE_ALL_STATIC
                signedRequestMode: REQUIRE_TOKENS
                signedRequestKeyset: LONG_KEYSET_NAME
    

###  URL query parameters 
    
    
    name: SERVICE_NAME
    routing:
      hostRules:
      - hosts:
        - DOMAIN_NAME
        pathMatcher: routes
      pathMatchers:
        - name: "ROUTE_NAME"
          routeRules:
          - priority: 1
            description: "ROUTE_DESCRIPTION"
            origin: "ORIGIN_NAME"
            matchRules:
            - pathTemplateMatch: "/HLS_PRIMARY_PLAYLIST.m3u8" # HLS primary playlists
            routeAction:
              cdnPolicy:
                cacheMode: CACHE_ALL_STATIC
                signedRequestMode: REQUIRE_TOKENS
                signedRequestKeyset: SHORT_KEYSET_NAME
                signedRequestMaximumExpirationTtl: SIGNED_REQUEST_MAXIMUM_EXPIRATION_TIME
                signedTokenOptions:
                  tokenQueryParameter: SHORT_TOKEN_NAME
                addSignatures:
                  actions:
                    - GENERATE_TOKEN_HLS_COOKIELESS
                  keyset: LONG_KEYSET_NAME
                  tokenTtl: TOKEN_EXPIRATION_TIME
                  tokenQueryParameter: LONG_TOKEN_NAME
                  copiedParameters:
                    - PathGlobs
                    - SessionID
          - priority: 2
            description: "PLAYLIST_ROUTE_DESCRIPTION"
            origin: "ORIGIN_NAME"
            matchRules:
            - pathTemplateMatch: "/**.m3u8" # HLS media playlists
            routeAction:
              cdnPolicy:
                cacheMode: CACHE_ALL_STATIC
                signedRequestMode: REQUIRE_TOKENS
                signedRequestKeyset: LONG_KEYSET_NAME
                addSignatures:
                  actions:
                    - PROPAGATE_TOKEN_HLS_COOKIELESS
          - priority: 3
            description: "SEGMENTS_ROUTE_DESCRIPTION"
            origin: "ORIGIN_NAME"
            matchRules:
            - pathTemplateMatch: "/**.ts" # HLS segments
            routeAction:
              cdnPolicy:
                cacheMode: CACHE_ALL_STATIC
                signedRequestMode: REQUIRE_TOKENS
                signedRequestKeyset: LONG_KEYSET_NAME
    

## Generate short-duration tokens at your application server

For information about generating tokens, see [Generate tokens](https://docs.cloud.google.com/media-cdn/docs/generate-tokens).

## Apply defense-in-depth content protections

As a best practice, enable origin authentication as follows:

  * For Cloud Storage, use [Identity and Access Management permissions with private Cloud Storage buckets](https://docs.cloud.google.com/media-cdn/docs/origins#private-storage-buckets).

  * For AWS-compatible storage providers, use [AWS Signature Version 4](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html). Using origin authentication blocks requests that attempt to circumvent Media CDN and access your origin directly.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
