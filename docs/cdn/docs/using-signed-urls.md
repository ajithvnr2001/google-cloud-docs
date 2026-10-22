---
url: https://docs.cloud.google.com/cdn/docs/using-signed-urls/
title: Use signed URLs \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:52.745061+00:00
---

# Use signed URLs  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/using-signed-urls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  Use signed URLs Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of signed URLs and instructions for using them with Cloud CDN. Signed URLs give time-limited resource access to anyone in possession of the URL, regardless of whether the user has a Google Account.

A signed URL is a URL that provides limited permission and time to make a request. Signed URLs contain authentication information in their query strings, allowing users without credentials to perform specific actions on a resource. When you generate a signed URL, you specify a user or service account that must have sufficient permission to make the request associated with the URL.

After you generate a signed URL, anyone who possesses it can use the signed URL to perform specified actions (such as reading an object) within a specified period of time.

Signed URLs also support an optional `URLPrefix` parameter, allowing you to provide access to multiple URLs based on a common prefix.

If you want to scope access to a specific URL prefix, consider [using signed cookies](https://docs.cloud.google.com/cdn/docs/using-signed-cookies).

**Note:** You cannot configure signed URLs directly in the URL map. You must configure signed URLs on backend services or backend buckets.

## Before you begin

Before you use signed URLs, do the following:

  * Ensure that Cloud CDN is enabled; for instructions, see [Using Cloud CDN](https://docs.cloud.google.com/cdn/docs/using-cdn). You can configure signed URLs on a backend before enabling Cloud CDN, but there is no effect until Cloud CDN is enabled.

  * If necessary, update to the latest version of the Google Cloud CLI:
        
        gcloud components update
        




For an overview, see [Signed URLs and signed cookies](https://docs.cloud.google.com/cdn/docs/private-content).

## Configure signed request keys

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
    

## Sign URLs

The last step is to sign URLs and distribute them. You can sign URLs by using the `gcloud compute sign-url` command or by using code that you write yourself. If you need many signed URLs, custom code provides better performance.

**Note:** The host and path components of URLs are used to validate signatures. When you provide the URL to `gcloud` or to programmatic APIs, omit the port. In other words, for a path like `https://example.com:443/path`, specify the path as `https://example.com/path`. Otherwise, the generated signature won't match the value that Cloud CDN computes.

### Create signed URLs

Use these instructions to create signed URLs by using the `gcloud compute sign-url` command. This step assumes that you have already [created the keys](https://docs.cloud.google.com/cdn/docs/using-signed-urls#createkeys).

###  Console 

You cannot create signed URLs by using the Google Cloud console. You can use the Google Cloud CLI or write custom code by using the following examples.

###  gcloud 

The Google Cloud CLI includes a command for signing URLs. The command implements the algorithm described in the section about writing your own code.
    
    
    gcloud compute sign-url \
      "URL" \
      --key-name KEY_NAME \
      --key-file KEY_FILE_NAME \
      --expires-in TIME_UNTIL_EXPIRATION \
      [--validate]
    

This command reads and decodes the [base64url encoded](https://tools.ietf.org/html/rfc4648#section-5) key value from `KEY_FILE_NAME`, and then outputs a signed URL that you can use for `GET` or `HEAD` requests for the given URL.

For example:
    
    
    gcloud compute sign-url \
      "https://example.com/media/video.mp4" \
      --key-name my-test-key \
      --expires-in 30m \
      --key-file sign-url-key-file
    

The `URL` must be a valid URL that has a path component. For example, `http://example.com` is invalid, but `https://example.com/` and `https://example.com/whatever` are both valid URLs.

If the optional `--validate` flag is given, this command sends a `HEAD` request with the resulting URL, and prints the HTTP response code. If the signed URL is correct, the response code is the same as the result code sent by your backend. If the response code isn't the same, recheck `KEY_NAME` and the contents of the specified file, and make sure that the value of `TIME_UNTIL_EXPIRATION` is at least several seconds.

If the `--validate`flag is not given, the following are not verified:

  * The inputs
  * The generated URL
  * The generated signed URL



### Programmatically create signed URLs

The following code samples demonstrate how to programmatically create signed URLs.

### Go
    
    
    import (
    	"crypto/hmac"
    	"crypto/sha1"
    	"encoding/base64"
    	"fmt"
    	"io"
    	"io/ioutil"
    	"os"
    	"strings"
    	"time"
    )
    
    // SignURL creates a signed URL for an endpoint on Cloud CDN.
    //
    // - url must start with "https://" and should not have the "Expires", "KeyName", or "Signature"
    // query parameters.
    // - key should be in raw form (not base64url-encoded) which is 16-bytes long.
    // - keyName must match a key added to the backend service or bucket.
    func signURL(url, keyName string, key []byte, expiration time.Time) string {
    	sep := "?"
    	if strings.Contains(url, "?") {
    		sep = "&"
    	}
    	url += sep
    	url += fmt.Sprintf("Expires=%d", expiration.Unix())
    	url += fmt.Sprintf("&KeyName=%s", keyName)
    
    	mac := hmac.New(sha1.New, key)
    	mac.Write([]byte(url))
    	sig := base64.URLEncoding.EncodeToString(mac.Sum(nil))
    	url += fmt.Sprintf("&Signature=%s", sig)
    	return url
    }
    

### Ruby
    
    
    def signed_url url:, key_name:, key:, expiration:
      # url        = "URL of the endpoint served by Cloud CDN"
      # key_name   = "Name of the signing key added to the Google Cloud Storage bucket or service"
      # key        = "Signing key as urlsafe base64 encoded string"
      # expiration = Ruby Time object with expiration time
    
      require "base64"
      require "openssl"
      require "time"
    
      # Decode the URL safe base64 encode key
      decoded_key = Base64.urlsafe_decode64 key
    
      # Get UTC time in seconds
      expiration_utc = expiration.utc.to_i
    
      # Determine which separator makes sense given a URL
      separator = "?"
      separator = "&" if url.include? "?"
    
      # Concatenate url with expected query parameters Expires and KeyName
      url = "#{url}#{separator}Expires=#{expiration_utc}&KeyName=#{key_name}"
    
      # Sign the url using the key and url safe base64 encode the signature
      signature         = OpenSSL::HMAC.digest "SHA1", decoded_key, url
      encoded_signature = Base64.urlsafe_encode64 signature
    
      # Concatenate the URL and encoded signature
      signed_url = "#{url}&Signature=#{encoded_signature}"
    end

### .NET
    
    
    /// <summary>
    /// Creates signed URL for Google Cloud SDN
    /// More details about order of operations is here: 
    /// <see cref="https://cloud.google.com/cdn/docs/using-signed-urls#programmatically_creating_signed_urls"/>
    /// </summary>
    /// <param name="url">The Url to sign. This URL can't include Expires and KeyName query parameters in it</param>
    /// <param name="keyName">The name of the key used to sign the URL</param>
    /// <param name="encodedKey">The key used to sign the Url</param>
    /// <param name="expirationTime">Expiration time of the signature</param>
    /// <returns>Signed Url that is valid until {expirationTime}</returns>
    public static string CreateSignedUrl(string url, string keyName, string encodedKey, DateTime expirationTime)
    {
        var builder = new UriBuilder(url);
    
        long unixTimestampExpiration = ToUnixTime(expirationTime);
    
        char queryParam = string.IsNullOrEmpty(builder.Query) ? '?' : '&';
        builder.Query += $"{queryParam}Expires={unixTimestampExpiration}&KeyName={keyName}".ToString();
    
        // Key is passed as base64url encoded
        byte[] decodedKey = Base64UrlDecode(encodedKey);
    
        // Computes HMAC SHA-1 hash of the URL using the key
        byte[] hash = ComputeHash(decodedKey, builder.Uri.AbsoluteUri);
        string encodedHash = Base64UrlEncode(hash);
    
        builder.Query += $"&Signature={encodedHash}";
        return builder.Uri.AbsoluteUri;
    }
    
    private static long ToUnixTime(DateTime date)
    {
        var epoch = new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc);
        return Convert.ToInt64((date - epoch).TotalSeconds);
    }
    
    private static byte[] Base64UrlDecode(string arg)
    {
        string s = arg;
        s = s.Replace('-', '+'); // 62nd char of encoding
        s = s.Replace('_', '/'); // 63rd char of encoding
    
        return Convert.FromBase64String(s); // Standard base64 decoder
    }
    
    private static string Base64UrlEncode(byte[] inputBytes)
    {
        var output = Convert.ToBase64String(inputBytes);
    
        output = output.Replace('+', '-')      // 62nd char of encoding
                       .Replace('/', '_');     // 63rd char of encoding
    
        return output;
    }
    
    private static byte[] ComputeHash(byte[] secretKey, string signatureString)
    {
        var enc = Encoding.ASCII;
        using (HMACSHA1 hmac = new HMACSHA1(secretKey))
        {
            hmac.Initialize();
    
            byte[] buffer = enc.GetBytes(signatureString);
    
            return hmac.ComputeHash(buffer);
        }
    }
    

### Java
    
    
    /** Samples to create a signed URL for a Cloud CDN endpoint */
    public class SignedUrls {
    
      /**
       * Creates a signed URL for a Cloud CDN endpoint with the given key
       * URL must start with http:// or https://, and must contain a forward
       * slash (/) after the hostname.
       *
       * @param url the Cloud CDN endpoint to sign
       * @param key url signing key uploaded to the backend service/bucket, as a 16-byte array
       * @param keyName the name of the signing key added to the back end bucket or service
       * @param expirationTime the date that the signed URL expires
       * @return a properly formatted signed URL
       * @throws InvalidKeyException when there is an error generating the signature for the input key
       * @throws NoSuchAlgorithmException when HmacSHA1 algorithm is not available in the environment
       */
      public static String signUrl(String url,
                                   byte[] key,
                                   String keyName,
                                   Date expirationTime)
              throws InvalidKeyException, NoSuchAlgorithmException {
    
        final long unixTime = expirationTime.getTime() / 1000;
    
        String urlToSign = url
                            + (url.contains("?") ? "&" : "?")
                            + "Expires=" + unixTime
                            + "&KeyName=" + keyName;
    
        String encoded = SignedUrls.getSignature(key, urlToSign);
        return urlToSign + "&Signature=" + encoded;
      }
    
      public static String getSignature(byte[] privateKey, String input)
          throws InvalidKeyException, NoSuchAlgorithmException {
    
        final String algorithm = "HmacSHA1";
        final int offset = 0;
        Key key = new SecretKeySpec(privateKey, offset, privateKey.length, algorithm);
        Mac mac = Mac.getInstance(algorithm);
        mac.init(key);
        return  Base64.getUrlEncoder().encodeToString(mac.doFinal(input.getBytes()));
      }

### Python
    
    
    import argparse
    import base64
    from datetime import datetime, timezone
    import hashlib
    import hmac
    from urllib.parse import parse_qs, urlsplit
    
    
    def sign_url(
        url: str,
        key_name: str,
        base64_key: str,
        expiration_time: datetime,
    ) -> str:
        """Gets the Signed URL string for the specified URL and configuration.
    
        Args:
            url: URL to sign.
            key_name: name of the signing key.
            base64_key: signing key as a base64 encoded string.
            expiration_time: expiration time as time-zone aware datetime.
    
        Returns:
            Returns the Signed URL appended with the query parameters based on the
            specified configuration.
        """
        stripped_url = url.strip()
        parsed_url = urlsplit(stripped_url)
        query_params = parse_qs(parsed_url.query, keep_blank_values=True)
        epoch = datetime.fromtimestamp(0, timezone.utc)
        expiration_timestamp = int((expiration_time - epoch).total_seconds())
        decoded_key = base64.urlsafe_b64decode(base64_key)
    
        url_to_sign = f"{stripped_url}{'&' if query_params else '?'}Expires={expiration_timestamp}&KeyName={key_name}"
    
        digest = hmac.new(decoded_key, url_to_sign.encode("utf-8"), hashlib.sha1).digest()
        signature = base64.urlsafe_b64encode(digest).decode("utf-8")
    
        return f"{url_to_sign}&Signature={signature}"
    
    

### PHP
    
    
    /**
     * Decodes base64url (RFC4648 Section 5) string
     *
     * @param string $input base64url encoded string
     *
     * @return string
     */
    function base64url_decode($input)
    {
        $input .= str_repeat('=', (4 - strlen($input) % 4) % 4);
        return base64_decode(strtr($input, '-_', '+/'), true);
    }
    
    /**
    * Encodes a string with base64url (RFC4648 Section 5)
    * Keeps the '=' padding by default.
    *
    * @param string $input   String to be encoded
    * @param bool   $padding Keep the '=' padding
    *
    * @return string
    */
    function base64url_encode($input, $padding = true)
    {
        $output = strtr(base64_encode($input), '+/', '-_');
        return ($padding) ? $output : str_replace('=', '',  $output);
    }
    
    /**
     * Creates signed URL for Google Cloud CDN
     * Details about order of operations: https://cloud.google.com/cdn/docs/using-signed-urls#creating_signed_urls
     *
     * Example function invocation (In production store the key safely with other secrets):
     *
     *     <?php
     *     $base64UrlKey = 'wpLL7f4VB9RNe_WI0BBGmA=='; // head -c 16 /dev/urandom | base64 | tr +/ -_
     *     $signedUrl = sign_url('https://example.com/foo', 'my-key', $base64UrlKey, time() + 1800);
     *     echo $signedUrl;
     *     ?>
     *
     * @param string $url             URL of the endpoint served by Cloud CDN
     * @param string $keyName         Name of the signing key added to the Google Cloud Storage bucket or service
     * @param string $base64UrlKey    Signing key as base64url (RFC4648 Section 5) encoded string
     * @param int    $expirationTime  Expiration time as a UNIX timestamp (GMT, e.g. time())
     *
     * @return string
     */
    function sign_url($url, $keyName, $base64UrlKey, $expirationTime)
    {
        // Decode the key
        $decodedKey = base64url_decode($base64UrlKey);
    
        // Determine which separator makes sense given a URL
        $separator = (strpos($url, '?') === false) ? '?' : '&';
    
        // Concatenate url with expected query parameters Expires and KeyName
        $url = "{$url}{$separator}Expires={$expirationTime}&KeyName={$keyName}";
    
        // Sign the url using the key and encode the signature using base64url
        $signature = hash_hmac('sha1', $url, $decodedKey, true);
        $encodedSignature = base64url_encode($signature);
    
        // Concatenate the URL and encoded signature
        return "{$url}&Signature={$encodedSignature}";
    }

### Programmatically create signed URLs with a URL prefix

The following code samples demonstrate how to programmatically create signed URLs with a URL prefix.

### Go
    
    
    import (
    	"crypto/hmac"
    	"crypto/sha1"
    	"encoding/base64"
    	"fmt"
    	"io"
    	"io/ioutil"
    	"os"
    	"strings"
    	"time"
    )
    
    // SignURLWithPrefix creates a signed URL prefix for an endpoint on Cloud CDN.
    // Prefixes allow access to any URL with the same prefix, and can be useful for
    // granting access broader content without signing multiple URLs.
    //
    // - urlPrefix must start with "https://" and should not include query parameters.
    // - key should be in raw form (not base64url-encoded) which is 16-bytes long.
    // - keyName must match a key added to the backend service or bucket.
    func signURLWithPrefix(urlPrefix, keyName string, key []byte, expiration time.Time) (string, error) {
    	if strings.Contains(urlPrefix, "?") {
    		return "", fmt.Errorf("urlPrefix must not include query params: %s", urlPrefix)
    	}
    
    	encodedURLPrefix := base64.URLEncoding.EncodeToString([]byte(urlPrefix))
    	input := fmt.Sprintf("URLPrefix=%s&Expires=%d&KeyName=%s",
    		encodedURLPrefix, expiration.Unix(), keyName)
    
    	mac := hmac.New(sha1.New, key)
    	mac.Write([]byte(input))
    	sig := base64.URLEncoding.EncodeToString(mac.Sum(nil))
    
    	signedValue := fmt.Sprintf("%s&Signature=%s", input, sig)
    
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
    
    public class SignedUrlWithPrefix {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
    
        // The name of the signing key must match a key added to the back end bucket or service.
        String keyName = "YOUR-KEY-NAME";
        // Path to the URL signing key uploaded to the backend service/bucket.
        String keyPath = "/path/to/key";
        // The date that the signed URL expires.
        long expirationTime = ZonedDateTime.now().plusDays(1).toEpochSecond();
        // URL of request
        String requestUrl = "https://media.example.com/videos/id/main.m3u8?userID=abc123&starting_profile=1";
        // URL prefix to sign as a string. URL prefix must start with either "http://" or "https://"
        // and must not include query parameters.
        String urlPrefix = "https://media.example.com/videos/";
    
        // Read the key as a base64 url-safe encoded string, then convert to byte array.
        // Key used in signing must be in raw form (not base64url-encoded).
        String base64String = new String(Files.readAllBytes(Paths.get(keyPath)),
            StandardCharsets.UTF_8);
        byte[] keyBytes = Base64.getUrlDecoder().decode(base64String);
    
        // Sign the url with prefix
        String signUrlWithPrefixResult = signUrlWithPrefix(requestUrl,
            urlPrefix, keyBytes, keyName, expirationTime);
        System.out.println(signUrlWithPrefixResult);
      }
    
      // Creates a signed URL with a URL prefix for a Cloud CDN endpoint with the given key. Prefixes
      // allow access to any URL with the same prefix, and can be useful for granting access broader
      // content without signing multiple URLs.
      static String signUrlWithPrefix(String requestUrl, String urlPrefix, byte[] key, String keyName,
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
          throw new IllegalArgumentException("urlPrefix malformed: " + urlPrefix);
        }
    
        String encodedUrlPrefix = Base64.getUrlEncoder().encodeToString(urlPrefix.getBytes(
            StandardCharsets.UTF_8));
        String urlToSign = "URLPrefix=" + encodedUrlPrefix
            + "&Expires=" + expirationTime
            + "&KeyName=" + keyName;
    
        String encoded = getSignatureForUrl(key, urlToSign);
        return requestUrl + "&" + urlToSign + "&Signature=" + encoded;
      }
    
      // Creates signature for input url with private key.
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
    
    
    def sign_url_prefix(
        url: str,
        url_prefix: str,
        key_name: str,
        base64_key: str,
        expiration_time: datetime,
    ) -> str:
        """Gets the Signed URL string for the specified URL prefix and configuration.
    
        Args:
            url: URL of request.
            url_prefix: URL prefix to sign.
            key_name: name of the signing key.
            base64_key: signing key as a base64 encoded string.
            expiration_time: expiration time as time-zone aware datetime.
    
        Returns:
            Returns the Signed URL appended with the query parameters based on the
            specified URL prefix and configuration.
        """
        stripped_url = url.strip()
        parsed_url = urlsplit(stripped_url)
        query_params = parse_qs(parsed_url.query, keep_blank_values=True)
        encoded_url_prefix = base64.urlsafe_b64encode(
            url_prefix.strip().encode("utf-8")
        ).decode("utf-8")
        epoch = datetime.fromtimestamp(0, timezone.utc)
        expiration_timestamp = int((expiration_time - epoch).total_seconds())
        decoded_key = base64.urlsafe_b64decode(base64_key)
    
        policy = f"URLPrefix={encoded_url_prefix}&Expires={expiration_timestamp}&KeyName={key_name}"
    
        digest = hmac.new(decoded_key, policy.encode("utf-8"), hashlib.sha1).digest()
        signature = base64.urlsafe_b64encode(digest).decode("utf-8")
    
        return f"{stripped_url}{'&' if query_params else '?'}{policy}&Signature={signature}"
    
    

### Generate custom signed URLs

When you write your own code to generate signed URLs, your goal is to create URLs with the following format or algorithm; all URL parameters are case-sensitive and must be in the order shown:
    
    
    https://example.com/foo?Expires=EXPIRATION&KeyName=KEY_NAME&Signature=SIGNATURE
    

To generate signed URLs, follow these steps:

  1. Ensure that the URL for signing does not have a `Signature` query parameter.

  2. Determine when the URL expires and append an `Expires` query parameter with the required expiration time in [UTC time](https://wikipedia.org/wiki/Unix_time) (the number of seconds since 1970-01-01 00:00:00 UTC). To maximize security, set the value to the shortest time period possible for your use case. The longer a signed URL is valid, the bigger the risk that the user that you give it to shares it with others, accidentally or otherwise.

  3. Set the key name. The URL must be signed with a key of the backend service or backend bucket that serves the URL. It is best to use the most recently added key for key rotation. Add the key to the URL by appending `&KeyName=KEY_NAME`. Replace `KEY_NAME` with the name of the chosen key created in [Creating signed request keys](https://docs.cloud.google.com/cdn/docs/using-signed-urls#createkeys).

  4. Sign the URL. Create the signed URL by following these steps. Make sure that the query parameters are in the order shown immediately before step 1, and make sure that nothing in the signed URL changes case.

a. Hash the entire URL (including `http://` or `https://` at the beginning and `&KeyName...` at the end) with HMAC-SHA1 by using the secret key that corresponds to the key name chosen earlier. Use the raw 16-byte secret key, not the base64url encoded key. Decode it if needed.

b. Use [base64url encode](https://tools.ietf.org/html/rfc4648#section-5) to encode the result.

c. Append `&Signature=` to the URL, followed by the encoded signature. Don't convert trailing `=` characters of the signature to their percent-encoded form, `%3D`.




### Use URL prefixes for signed URLs

Instead of signing the full request URL with the `Expires` and `KeyName` query parameters, you can instead sign the `URLPrefix`, `Expires`, and `KeyName` query parameters only. This allows a given combination of `URLPrefix`, `Expires`, `KeyName`, and `Signature` query parameters to be reused verbatim across multiple URLs that match the `URLPrefix`, avoiding the need to create a new signature for each distinct URL.

In the following example, the highlighted text shows the parameters that you sign. The `Signature` is appended as the final query parameter, as usual.
    
    
    https://media.example.com/videos/id/master.m3u8?userID=abc123&starting_profile=1&URLPrefix=aHR0cHM6Ly9tZWRpYS5leGFtcGxlLmNvbS92aWRlb3Mv&Expires=1566268009&KeyName=mySigningKey&Signature=8NBSdQGzvDftrOIa3WHpp646Iis=

Unlike signing a full request URL, when you sign with `URLPrefix` you aren't signing any query parameters, so query parameters can be freely included in the URL. And, unlike full request URL signatures, those additional query parameters can appear both before and after the query parameters that make up the signature. As a result, the following is also a valid URL with a signed URL prefix:
    
    
    https://media.example.com/videos/id/master.m3u8?userID=abc123&URLPrefix=aHR0cHM6Ly9tZWRpYS5leGFtcGxlLmNvbS92aWRlb3Mv&Expires=1566268009&KeyName=mySigningKey&Signature=8NBSdQGzvDftrOIa3WHpp646Iis=&starting_profile=1
    

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

### Validate signed URLs

The process of validating a signed URL is essentially the same as generating a signed URL. For example, suppose that you want to validate the following signed URL:
    
    
    https://example.com/PATH?Expires=EXPIRATION&KeyName=KEY_NAME&Signature=SIGNATURE
    

You can use the secret key named by `KEY_NAME` to independently generate the signature for the following URL:
    
    
    https://example.com/PATH?Expires=EXPIRATION&KeyName=KEY_NAME
    

Then you can verify that it matches `SIGNATURE`.

Suppose that you want to validate a signed URL that has a `URLPrefix`, as shown here:
    
    
    https://example.com/PATH?URLPrefix=URL_PREFIX&Expires=EXPIRATION&KeyName=KEY_NAME&Signature=SIGNATURE
    

First, verify that the base64-decoded value of `URL_PREFIX` is a prefix of `https://example.com/PATH`. If so, you can then calculate the signature for the following:
    
    
    URLPrefix=URL_PREFIX&Expires=EXPIRATION&KeyName=KEY_NAME
    

You can then verify that it matches `SIGNATURE`.

For URL-based signing methods, where the signature is part of the query parameters or embedded as a URL path component, the signature and related parameters are removed from the URL before the request is sent to the origin. This prevents the signature from causing routing issues when the origin is handling the request. To validate these requests, you can inspect the `x-client-request-url` request header, which includes the original (signed) client request URL prior to the removal of the signed components.

### Remove public access to the Cloud Storage bucket

For signed URLs to properly protect content, it is important that the origin server not grant public access to that content. When using a Cloud Storage bucket, a common approach is to make objects public temporarily for testing purposes. After enabling signed URLs, it's important to remove the `allUsers` (and `allAuthenticatedUsers`, if applicable) READ permissions (in other words, the [Storage Object Viewer](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) Identity and Access Management role) on the bucket.

After you disable public access on the bucket, individual users can still access Cloud Storage without signed URLs if they have access permission, such as OWNER permission.

To remove public `allUsers` READ access on a Cloud Storage bucket, reverse the action described in [Making all objects in a bucket publicly readable](https://docs.cloud.google.com/storage/docs/access-control/making-data-public#buckets).

### Distribute and use signed URLs

The URL returned from the Google Cloud CLI or produced by your custom code can be distributed according to your needs. We recommend signing only HTTPS URLs, because HTTPS provides a secure transport that prevents the `Signature` component of the signed URL from being intercepted. Similarly, make sure that you distribute the signed URLs over secure transport protocols such as TLS/HTTPS.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
