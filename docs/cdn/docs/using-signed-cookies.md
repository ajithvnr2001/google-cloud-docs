---
url: https://docs.cloud.google.com/cdn/docs/using-signed-cookies/
title: Use signed cookies \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:52.264245+00:00
---

# Use signed cookies  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/using-signed-cookies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  Use signed cookies Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of signed cookies and instructions for using them with Cloud CDN. Signed cookies give time-limited resource access to a set of files, regardless of whether the users have Google Accounts.

Signed cookies are an alternative to signed URLs. Signed cookies protect access when separately signing tens or hundreds of URLs for each user isn't feasible in your application.

Signed cookies let you do the following:

  * Authorize a user and provide them with a time-limited token for accessing your protected content (instead of signing each URL).
  * Scope the user's access to a specific URL prefix, such as `https://media.example.com/videos/`, and grant the authorized user access to protected content within that URL prefix only.
  * Keep your URLs and media manifests unchanged, simplifying your packaging pipeline and improving cacheability.



If you want to scope access to specific URLs instead, consider [using signed URLs](https://docs.cloud.google.com/cdn/docs/using-signed-urls).

**Note:** You cannot configure signed cookies directly in the URL map. You must configure signed cookies on backend services or backend buckets.

## Before you begin

Before you use signed cookies, do the following:

  * Ensure that Cloud CDN is enabled; for instructions, see [Using Cloud CDN](https://docs.cloud.google.com/cdn/docs/using-cdn). You can configure signed cookies on a backend before enabling Cloud CDN, but there is no effect until Cloud CDN is enabled.

  * If necessary, update to the latest version of the Google Cloud CLI:
        
        gcloud components update
        




For an overview, see [Signed URLs and signed cookies](https://docs.cloud.google.com/cdn/docs/private-content).

## Configuring signed request keys

Creating keys for your signed URLs or signed cookies requires several steps, which are described in the following sections.

### Security considerations

**Important:** You must configure your origin web servers to validate the signatures on every signed request that they serve, and accept or reject unsigned requests.

Cloud CDN does _not_ validate requests in the following circumstances:

  * The request is not signed.
  * The backend service or backend bucket for the request doesn't have Cloud CDN enabled.



Signed requests must _always_ be validated at the origin before serving the response. This is because origins can be used for serving a mixture of signed and unsigned content and because a client might access the origin directly.

  * Cloud CDN doesn't block requests without a `Signature` query parameter or `Cloud-CDN-Cookie` HTTP cookie. It rejects requests with invalid (or otherwise malformed) request parameters.
  * When your application detects an invalid signature, make sure that your application responds with an `HTTP 403 (Unauthorized)` response code. `HTTP 403` response codes aren't cacheable.
  * Responses to signed and unsigned requests are cached separately, so a successful response to a valid signed request is never used to serve an unsigned request.
  * If your application sends a cacheable response code to an invalid request, valid future requests might be incorrectly rejected.



For Cloud Storage backends, make sure to [remove public access](https://docs.cloud.google.com/cdn/docs/using-signed-urls#removing-public-access), so that Cloud Storage can reject requests that are missing a valid signature.

The following table summarizes the behavior.

Request has signature | Cache hit | Behavior  
---|---|---  
No | No | Forward to backend origin.  
No | Yes | Serve from cache.  
Yes | No | Validate signature. If valid, forward to backend origin.  
Yes | Yes | Validate signature. If valid, serve from cache.  
  
### Create signed request keys

You enable support for Cloud CDN signed URLs and signed cookies by creating one or more keys on a Cloud CDN-enabled [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service), [backend bucket](https://docs.cloud.google.com/load-balancing/docs/https/ext-load-balancer-backend-buckets), or both.

For each backend service or backend bucket, you can create and delete keys as your security needs dictate. Each backend can have up to three keys configured at a time. We suggest periodically rotating your keys by deleting the oldest, adding a new key, and using the new key when signing URLs or cookies.

You can use the same key name in multiple backend services and backend buckets because each set of keys is independent of the others. Key names can be up to 63 characters. To name your keys, use the characters A-Z, a-z, 0-9, _ (underscore), and - (hyphen).

When you create keys, be sure to keep them secure because anyone who has one of your keys can create signed URLs or signed cookies that Cloud CDN accepts until the key is deleted from Cloud CDN. The keys are stored on the computer where you generate the signed URLs or signed cookies. Cloud CDN also stores the keys to verify request signatures.

To keep the keys secret, the key values aren't included in responses to any API requests. If you lose a key, you must create a new one.

**Important:** Keep the generated key file private, and do not expose it to users or store it directly in source code. Consider using a secrets storage mechanism such as [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs) to encrypt the key and provide access to only trusted applications.

To create a signed request key, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud CDN** page. 

[Go to Cloud CDN](https://console.cloud.google.com/networking/cdn/list)

  2. Click the name of the origin that you want to add the key to.
  3. On the **Origin details** page, click the **Edit** button.
  4. In the **Origin basics** section, click **Next** to open the **Host and path rules** section.
  5. In the **Host and path rules** section, click **Next** to open the **Cache performance** section.
  6. In the **Restricted content** section, select **Restrict access using signed URLs and signed cookies**.
  7. Click **Add signing key**.

     1. Specify a unique name for the new signing key.
     2. In the **Key creation method** section, select **Automatically generate**. Alternatively, click **Let me enter** , and then specify a signing key value.

For the former option, copy the automatically generated signing key value to a private file, which you can use to [create signed URLs](https://docs.cloud.google.com/cdn/docs/using-signed-urls#create_signed_urls).

     3. Click **Done**.

     4. In the **Cache entry maximum age** section, enter a value, and then select a unit of time.

  8. Click **Done**.




###  gcloud 

The `gcloud` command-line tool reads keys from a local file that you specify. The key file must be created by generating strongly random 128 bits, encoding them with base64, and then replacing the character `+` with `-` and replacing the character `/` with `_`. For more information, see [RFC 4648](https://tools.ietf.org/html/rfc4648#section-5). It is vital that the key is strongly random. On a UNIX-like system, you can generate a strongly random key and store it in the key file with the following command:
    
    
    head -c 16 /dev/urandom | base64 | tr +/ -_ > KEY_FILE_NAME
    

To add the key to a backend service:
    
    
    gcloud compute backend-services \
       add-signed-url-key BACKEND_NAME \
       --key-name KEY_NAME \
       --key-file KEY_FILE_NAME
    

To add the key to a backend bucket:
    
    
    gcloud compute backend-buckets \
       add-signed-url-key BACKEND_NAME \
       --key-name KEY_NAME \
       --key-file KEY_FILE_NAME
    

**Note:** Even though the sub-command is `add-signed-url-key`, the key is a signed request key that works for both signed cookies and signed URLs.

### Configure Cloud Storage permissions

If you use Cloud Storage and you have restricted who can read the objects, you must give Cloud CDN permission to read the objects by adding the Cloud CDN service account to Cloud Storage ACLs.

You don't need to create the service account. The service account is created automatically the first time that you add a key to a backend bucket in a project.

Before you run the following command, add at least one key to a backend bucket in your project. Otherwise, the command fails with an error because the Cloud CDN cache fill service account is not created until you add one or more keys for the project.

**Note:** If your project has a [domain restricted sharing (DRS) organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) in the project, you can temporarily [disable the DRS policy](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/disable-enforce) before you run the [`gcloud storage buckets add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding) and [re-enable](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/enable-enforce) the policy. Alternatively, you can add the owning organization ID for the `cloud-cdn-fill` project to your allowlist. This permits the IAM binding while keeping the rest of your project restricted. Contact [support](https://cloud.google.com/support) if you need assistance identifying the ID.
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET \
      --member=serviceAccount:service-PROJECT_NUMBER@cloud-cdn-fill.iam.gserviceaccount.com \
      --role=roles/storage.objectViewer
    

Replace `PROJECT_NUMBER` with your project number and `BUCKET` with your storage bucket.

The Cloud CDN service account `service-PROJECT_NUMBER@cloud-cdn-fill.iam.gserviceaccount.com` doesn't appear in the list of service accounts in your project. This is because the Cloud CDN service account is owned by Cloud CDN, not your project.

For more information about project numbers, see [Locate the project ID and project number](https://support.google.com/cloud/answer/6158840) in the Google Cloud console Help documentation.

### Customize the maximum cache time

Cloud CDN caches responses for signed requests regardless of the backend's `Cache-Control` header. The maximum time that responses can be cached without revalidation is set by the `signed-url-cache-max-age` flag, which defaults to one hour and can be modified as shown here.

To set the maximum cache time for a backend service or backend bucket, run one of the following commands:
    
    
    gcloud compute backend-services update BACKEND_NAME \
      --signed-url-cache-max-age MAX_AGE
    
    
    
    gcloud compute backend-buckets update BACKEND_NAME \
      --signed-url-cache-max-age MAX_AGE
    

### List signed request key names

To list the keys on a backend service or backend bucket, run one of the following commands:
    
    
    gcloud compute backend-services describe BACKEND_NAME
    
    
    
    gcloud compute backend-buckets describe BACKEND_NAME
    

### Delete signed request keys

When URLs signed by a particular key should no longer be honored, run one of the following commands to delete that key from the backend service or backend bucket:
    
    
    gcloud compute backend-services \
       delete-signed-url-key BACKEND_NAME --key-name KEY_NAME
    
    
    
    gcloud compute backend-buckets \
       delete-signed-url-key BACKEND_NAME --key-name KEY_NAME
    

## Creating a policy

Signed cookie policies are a series of `key-value` pairs (delimited by the `:` character), similar to the query parameters used in a signed URL. For examples, see Issuing cookies to users.

Policies represent the parameters for which a request is valid. Policies are signed by using a hash-based message authentication code (HMAC) that Cloud CDN validates on each request.

### Defining policy format and fields

There are four required fields that you must define in the following order:

  * `URLPrefix`
  * `Expires`
  * `KeyName`
  * `Signature`



The `key-value` pairs in a signed cookie policy are case-sensitive.

#### URLPrefix

`URLPrefix` denotes a URL-safe base64 encoded URL prefix that encompasses all paths that the signature should be valid for.

A `URLPrefix` encodes a scheme (either `http://` or `https://`), FQDN, and an optional path. Ending the path with a `/` is optional but recommended. The prefix shouldn't include query parameters or fragments such as `?` or `#`.

For example, `https://media.example.com/videos` matches requests to both of the following:

  * `https://media.example.com/videos?video_id=138183&user_id=138138`
  * `https://media.example.com/videos/137138595?quality=low`



The prefix's path is used as a text substring, not strictly a directory path. For example, the prefix `https://example.com/data` grants access to both of the following:

  * `/data/file1`
  * `/database`



To avoid this mistake, we recommend ending all prefixes with `/` unless you intentionally choose to end the prefix with a partial filename such as `https://media.example.com/videos/123` to grant access to the following:

  * `/videos/123_chunk1`
  * `/videos/123_chunk2`
  * `/videos/123_chunkN`



If the requested URL doesn't match the `URLPrefix`, Cloud CDN rejects the request and returns an `HTTP 403` error to the client.

#### Expires

`Expires` must be a Unix timestamp (the number of seconds since January 1, 1970).

#### KeyName

`KeyName` is the key name for a key created against the backend bucket or backend service. Key names are case-sensitive.

#### Signature

`Signature` is the URL-safe base64 encoded HMAC-SHA-1 signature of the fields that make up the cookie policy. This is validated on each request; requests with an invalid signature are rejected with an `HTTP 403` error.

### Programmatically creating signed cookies

The following code samples demonstrate how to programmatically create signed cookies.

**Note:** Consider using [Secret Manager](https://docs.cloud.google.com/secret-manager/docs) for managing access to your signing keys.**Note:** The host and path components of the `URLPrefix` are used to validate signatures. When you provide the `URLPrefix` to programmatic APIs, omit the port. In other words, for a path like `https://example.com:443/path/`, specify the path as `https://example.com/path/`. Otherwise, the generated signature will not match the value that Cloud CDN computes.

### Go
    
    
    import (
    	"crypto/hmac"
    	"crypto/sha1"
    	"encoding/base64"
    	"fmt"
    	"io"
    	"io/ioutil"
    	"net/http"
    	"os"
    	"time"
    )
    
    // signCookie creates a signed cookie for an endpoint served by Cloud CDN.
    //
    // - urlPrefix must start with "https://" and should include the path prefix
    // for which the cookie will authorize access to.
    // - key should be in raw form (not base64url-encoded) which is
    // 16-bytes long.
    // - keyName must match a key added to the backend service or bucket.
    func signCookie(urlPrefix, keyName string, key []byte, expiration time.Time) (string, error) {
    	encodedURLPrefix := base64.URLEncoding.EncodeToString([]byte(urlPrefix))
    	input := fmt.Sprintf("URLPrefix=%s:Expires=%d:KeyName=%s",
    		encodedURLPrefix, expiration.Unix(), keyName)
    
    	mac := hmac.New(sha1.New, key)
    	mac.Write([]byte(input))
    	sig := base64.URLEncoding.EncodeToString(mac.Sum(nil))
    
    	signedValue := fmt.Sprintf("%s:Signature=%s",
    		input,
    		sig,
    	)
    
    	return signedValue, nil
    }
    

### Java
    
    
    import java.net.MalformedURLException;
    import java.net.URL;
    import java.nio.charset.StandardCharsets;
    import java.nio.file.Files;
    import java.nio.file.Paths;
    import java.security.InvalidKeyException;
    import java.security.Key;
    import java.security.NoSuchAlgorithmException;
    import java.time.ZonedDateTime;
    import java.util.Base64;
    import javax.crypto.Mac;
    import javax.crypto.spec.SecretKeySpec;
    
    public class SignedCookies {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
    
        // The name of the signing key must match a key added to the back end bucket or service.
        String keyName = "YOUR-KEY-NAME";
        // Path to the URL signing key uploaded to the backend service/bucket.
        String keyPath = "/path/to/key";
        // The Unix timestamp that the signed URL expires.
        long expirationTime = ZonedDateTime.now().plusDays(1).toEpochSecond();
        // URL prefix to sign as a string. URL prefix must start with either "http://" or "https://"
        // and must not include query parameters.
        String urlPrefix = "https://media.example.com/videos/";
    
        // Read the key as a base64 url-safe encoded string, then convert to byte array.
        // Key used in signing must be in raw form (not base64url-encoded).
        String base64String = new String(Files.readAllBytes(Paths.get(keyPath)),
            StandardCharsets.UTF_8);
        byte[] keyBytes = Base64.getUrlDecoder().decode(base64String);
    
        // Create signed cookie from policy.
        String signedCookie = signCookie(urlPrefix, keyBytes, keyName, expirationTime);
        System.out.println(signedCookie);
      }
    
      // Creates a signed cookie for the specified policy.
      public static String signCookie(String urlPrefix, byte[] key, String keyName,
          long expirationTime)
          throws InvalidKeyException, NoSuchAlgorithmException {
    
        // Validate input URL prefix.
        try {
          URL validatedUrlPrefix = new URL(urlPrefix);
          if (!validatedUrlPrefix.getProtocol().startsWith("http")) {
            throw new IllegalArgumentException(
                "urlPrefix must start with either http:// or https://: " + urlPrefix);
          }
          if (validatedUrlPrefix.getQuery() != null) {
            throw new IllegalArgumentException("urlPrefix must not include query params: " + urlPrefix);
          }
        } catch (MalformedURLException e) {
          throw new IllegalArgumentException(
              "urlPrefix malformed: " + urlPrefix);
        }
    
        String encodedUrlPrefix = Base64.getUrlEncoder().encodeToString(urlPrefix.getBytes(
            StandardCharsets.UTF_8));
        String policyToSign = String.format("URLPrefix=%s:Expires=%d:KeyName=%s", encodedUrlPrefix,
            expirationTime, keyName);
    
        String signature = getSignatureForUrl(key, policyToSign);
        return String.format("Cloud-CDN-Cookie=%s:Signature=%s", policyToSign, signature);
      }
    
      // Creates signature for input string with private key.
      private static String getSignatureForUrl(byte[] privateKey, String input)
          throws InvalidKeyException, NoSuchAlgorithmException {
    
        final String algorithm = "HmacSHA1";
        final int offset = 0;
        Key key = new SecretKeySpec(privateKey, offset, privateKey.length, algorithm);
        Mac mac = Mac.getInstance(algorithm);
        mac.init(key);
        return Base64.getUrlEncoder()
            .encodeToString(mac.doFinal(input.getBytes(StandardCharsets.UTF_8)));
      }
    }

### Python
    
    
    import argparse
    import base64
    from datetime import datetime, timezone
    import hashlib
    import hmac
    from urllib.parse import parse_qs, urlsplit
    
    
    def sign_cookie(
        url_prefix: str,
        key_name: str,
        base64_key: str,
        expiration_time: datetime,
    ) -> str:
        """Gets the Signed cookie value for the specified URL prefix and configuration.
    
        Args:
            url_prefix: URL prefix to sign.
            key_name: name of the signing key.
            base64_key: signing key as a base64 encoded string.
            expiration_time: expiration time as time-zone aware datetime.
    
        Returns:
            Returns the Cloud-CDN-Cookie value based on the specified configuration.
        """
        encoded_url_prefix = base64.urlsafe_b64encode(
            url_prefix.strip().encode("utf-8")
        ).decode("utf-8")
        epoch = datetime.fromtimestamp(0, timezone.utc)
        expiration_timestamp = int((expiration_time - epoch).total_seconds())
        decoded_key = base64.urlsafe_b64decode(base64_key)
    
        policy = f"URLPrefix={encoded_url_prefix}:Expires={expiration_timestamp}:KeyName={key_name}"
    
        digest = hmac.new(decoded_key, policy.encode("utf-8"), hashlib.sha1).digest()
        signature = base64.urlsafe_b64encode(digest).decode("utf-8")
    
        signed_policy = f"Cloud-CDN-Cookie={policy}:Signature={signature}"
    
        return signed_policy
    
    

### Validating signed cookies

The process of validating a signed cookie is essentially the same as generating a signed cookie. For example, suppose you want to validate the following signed cookie header:
    
    
    Cookie: Cloud-CDN-Cookie=URLPrefix=URL_PREFIX:Expires=EXPIRATION:KeyName=KEY_NAME:Signature=SIGNATURE; Domain=media.example.com; Path=/; Expires=Tue, 20 Aug 2019 02:26:49 GMT; HttpOnly
    

You can use the secret key named by `KEY_NAME` to independently generate the signature and then validate that it matches `SIGNATURE`.

## Issuing cookies to users

Your application must generate and issue each user (client) a single HTTP cookie containing a correctly signed policy:

  1. Create an HMAC-SHA-1 signer in your application code.

  2. Sign the policy by using the chosen key, taking note of the key name that you added to the backend, such as `mySigningKey`.

  3. Create a cookie policy with the following format, noting that both the name and value are case-sensitive:
         
         Name: Cloud-CDN-Cookie
         Value: URLPrefix=$BASE64URLECNODEDURLORPREFIX:Expires=$TIMESTAMP:KeyName=$KEYNAME:Signature=$BASE64URLENCODEDHMAC
         

Example `Set-Cookie` header:
         
         Set-Cookie: Cloud-CDN-Cookie=URLPrefix=aHR0cHM6Ly9tZWRpYS5leGFtcGxlLmNvbS92aWRlb3Mv:Expires=1566268009:KeyName=mySigningKey:Signature=0W2xlMlQykL2TG59UZnnHzkxoaw=; Domain=media.example.com; Path=/; Expires=Tue, 20 Aug 2019 02:26:49 GMT; HttpOnly
         

The `Domain` and `Path` attributes in the cookie determine whether the client sends the cookie to Cloud CDN.




### Recommendations and requirements

  * Explicitly set the `Domain` and `Path` attributes to match the domain and path prefix from which you intend to serve your protected content, which might differ from the domain and path where the cookie is issued (`example.com` versus `media.example.com` or `/browse` versus `/videos`).

  * Make sure that you have only one cookie with a given name for the same `Domain` and `Path`.

  * Ensure that you aren't issuing conflicting cookies because this might prevent access to content in other browser sessions (windows or tabs).

  * Set the `Secure` and `HttpOnly` flags where applicable. `Secure` ensures that the cookie is sent over HTTPS connections only. `HttpOnly` prevents making the cookie available to JavaScript.

  * The cookie attributes `Expires` and `Max-Age` are optional. If you omit them, the cookie exists while the browser session (tab, window) exists.

**Note:** The `Expires` attribute mentioned here is the one that (if present) appears outside of the cookie value. Don't confuse this attribute with the `Expires` parameter contained within the cookie value, which is required. The `Expires` parameter contained within the cookie value designates the time limit within which Cloud CDN allows the user to access protected content. This time limit is independent of the cookie lifespan.
  * On a cache fill or cache miss, the signed cookie is passed through to the origin that is defined in the backend service. Ensure that you are validating the signed cookie value on each request before serving content.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
