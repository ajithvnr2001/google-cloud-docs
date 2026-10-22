---
url: https://docs.cloud.google.com/media-cdn/docs/generate-tokens/
title: Generate tokens \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:04.507194+00:00
---

# Generate tokens  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/generate-tokens/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Generate tokens Stay organized with collections  Save and categorize content based on your preferences. 

This guide explains how to generate a token, and the required and optional fields for tokens.

To create a token, you compose a string to sign, which we refer to as a _signed value_ in this guide. The signed value includes parameters that describe the content you are protecting, the expiration time of the signed value, and so forth.

You use the signed value while creating a token string. You create a token string by composing the parameters for the token, such as a symmetric-key hash-based message authentication code (HMAC) of the signed value.

Media CDN uses the final composed token to help protect your content.

## Create a token

  1. Create a signed value by concatenating a string that contains the required token fields and desired optional token fields. Separate each field and any parameters with a tilde `~` character.

  2. Sign the signed value with either an Ed25519 signature or a [symmetric-key HMAC](https://docs.cloud.google.com/media-cdn/docs/use-dual-token-authentication#symmetric-key-hmac).

  3. Compose the token by concatenating a string that contains the required token fields and optional token fields. Separate each field and any parameters with a tilde `~` character.

When composing the token, the values for each of the parameters are the same between the signed value and the token string, with the following exceptions:

     * `FullPath`
     * `Headers`



The following code sample shows how to programmatically create a token:

### Python

To authenticate to Media CDN, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import base64
    import datetime
    import hashlib
    import hmac
    
    import cryptography.hazmat.primitives.asymmetric.ed25519 as ed25519
    
    
    def base64_encoder(value: bytes) -> str:
        """
        Returns a base64-encoded string compatible with Media CDN.
    
        Media CDN uses URL-safe base64 encoding and strips off the padding at the
        end.
        """
        encoded_bytes = base64.urlsafe_b64encode(value)
        encoded_str = encoded_bytes.decode("utf-8")
        return encoded_str.rstrip("=")
    
    
    def sign_token(
        base64_key: bytes,
        signature_algorithm: str,
        start_time: datetime.datetime = None,
        expiration_time: datetime.datetime = None,
        url_prefix: str = None,
        full_path: str = None,
        path_globs: str = None,
        session_id: str = None,
        data: str = None,
        headers: str = None,
        ip_ranges: str = None,
    ) -> str:
        """Gets the Signed URL Suffix string for the Media CDN' Short token URL requests.
        One of (`url_prefix`, `full_path`, `path_globs`) must be included in each input.
        Args:
            base64_key: Secret key as a base64 encoded string.
            signature_algorithm: Algorithm can be either `SHA1` or `SHA256` or `Ed25519`.
            start_time: Start time as a UTC datetime object.
            expiration_time: Expiration time as a UTC datetime object. If None, an expiration time 1 hour from now will be used.
            url_prefix: the URL prefix to sign, including protocol.
                        For example: http://example.com/path/ for URLs under /path or http://example.com/path?param=1
            full_path:  A full path to sign, starting with the first '/'.
                        For example: /path/to/content.mp4
            path_globs: a set of ','- or '!'-delimited path glob strings.
                        For example: /tv/*!/film/* to sign paths starting with /tv/ or /film/ in any URL.
            session_id: a unique identifier for the session
            data: data payload to include in the token
            headers: header name and value to include in the signed token in name=value format.  May be specified more than once.
                        For example: [{'name': 'foo', 'value': 'bar'}, {'name': 'baz', 'value': 'qux'}]
            ip_ranges: A list of comma separated ip ranges. Both IPv4 and IPv6 ranges are acceptable.
                        For example: "203.0.113.0/24,2001:db8:4a7f:a732/64"
    
        Returns:
            The Signed URL appended with the query parameters based on the
            specified URL prefix and configuration.
        """
    
        decoded_key = base64.urlsafe_b64decode(base64_key)
        algo = signature_algorithm.lower()
    
        # For most fields, the value we put in the token and the value we must sign
        # are the same.  The FullPath and Headers use a different string for the
        # value to be signed compared to the token.  To illustrate this difference,
        # we'll keep the token and the value to be signed separate.
        tokens = []
        to_sign = []
    
        # check for `full_path` or `path_globs` or `url_prefix`
        if full_path:
            tokens.append("FullPath")
            to_sign.append(f"FullPath={full_path}")
        elif path_globs:
            path_globs = path_globs.strip()
            field = f"PathGlobs={path_globs}"
            tokens.append(field)
            to_sign.append(field)
        elif url_prefix:
            field = "URLPrefix=" + base64_encoder(url_prefix.encode("utf-8"))
            tokens.append(field)
            to_sign.append(field)
        else:
            raise ValueError(
                "User Input Missing: One of `url_prefix`, `full_path` or `path_globs` must be specified"
            )
    
        # check & parse optional params
        if start_time:
            epoch_duration = start_time.astimezone(
                tz=datetime.timezone.utc
            ) - datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
            field = f"Starts={int(epoch_duration.total_seconds())}"
            tokens.append(field)
            to_sign.append(field)
    
        if not expiration_time:
            expiration_time = datetime.datetime.now() + datetime.timedelta(hours=1)
            epoch_duration = expiration_time.astimezone(
                tz=datetime.timezone.utc
            ) - datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
        else:
            epoch_duration = expiration_time.astimezone(
                tz=datetime.timezone.utc
            ) - datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
        field = f"Expires={int(epoch_duration.total_seconds())}"
        tokens.append(field)
        to_sign.append(field)
    
        if session_id:
            field = f"SessionID={session_id}"
            tokens.append(field)
            to_sign.append(field)
    
        if data:
            field = f"Data={data}"
            tokens.append(field)
            to_sign.append(field)
    
        if headers:
            header_names = []
            header_pairs = []
            for each in headers:
                header_names.append(each["name"])
                header_pairs.append("%s=%s" % (each["name"], each["value"]))
            tokens.append(f"Headers={','.join(header_names)}")
            to_sign.append(f"Headers={','.join(header_pairs)}")
    
        if ip_ranges:
            field = f"IPRanges={base64_encoder(ip_ranges.encode('ascii'))}"
            tokens.append(field)
            to_sign.append(field)
    
        # generating token
        to_sign = "~".join(to_sign)
        to_sign_bytes = to_sign.encode("utf-8")
        if algo == "ed25519":
            digest = ed25519.Ed25519PrivateKey.from_private_bytes(decoded_key).sign(
                to_sign_bytes
            )
            tokens.append("Signature=" + base64_encoder(digest))
        elif algo == "sha256":
            signature = hmac.new(
                decoded_key, to_sign_bytes, digestmod=hashlib.sha256
            ).hexdigest()
            tokens.append("hmac=" + signature)
        elif algo == "sha1":
            signature = hmac.new(
                decoded_key, to_sign_bytes, digestmod=hashlib.sha1
            ).hexdigest()
            tokens.append("hmac=" + signature)
        else:
            raise ValueError(
                "Input Missing Error: `signature_algorithm` can only be one of `sha1`, `sha256` or `ed25519`"
            )
        return "~".join(tokens)
    
    

### Java

To authenticate to Media CDN, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import java.nio.charset.StandardCharsets;
    import java.security.InvalidKeyException;
    import java.security.NoSuchAlgorithmException;
    import java.time.Instant;
    import java.time.format.DateTimeFormatter;
    import java.time.temporal.ChronoUnit;
    import java.util.ArrayList;
    import java.util.Base64;
    import java.util.List;
    import java.util.Optional;
    import javax.crypto.Mac;
    import javax.crypto.spec.SecretKeySpec;
    import org.bouncycastle.crypto.params.Ed25519PrivateKeyParameters;
    import org.bouncycastle.crypto.signers.Ed25519Signer;
    import org.bouncycastle.util.encoders.Hex;
    
    public class DualToken {
    
      public static void main(String[] args) throws NoSuchAlgorithmException, InvalidKeyException {
        // TODO(developer): Replace these variables before running the sample.
        // Secret key as a base64 encoded string.
        byte[] base64Key = new byte[]{};
        // Algorithm can be one of these: SHA1, SHA256, or Ed25519.
        String signatureAlgorithm = "ed25519";
        // (Optional) Start time as a UTC datetime object.
        DateTimeFormatter formatter = DateTimeFormatter.ISO_INSTANT;
        Optional<Instant> startTime = Optional.empty();
        // Expiration time as a UTC datetime object.
        // If None, an expiration time that's an hour after the current time is used.
        Instant expiresTime = Instant.from(formatter.parse("2022-09-13T12:00:00Z"));
    
        // ONE OF (`urlPrefix`, `fullPath`, `pathGlobs`) must be included in each input.
        // The URL prefix and protocol to sign.
        // For example: http://example.com/path/ for URLs under /path or http://example.com/path?param=1
        Optional<String> urlPrefix = Optional.empty();
        // A full path to sign, starting with the first '/'.
        // For example: /path/to/content.mp4
        Optional<String> fullPath = Optional.of("http://10.20.30.40/");
        // A set of path glob strings delimited by ',' or '!'.
        // For example: /tv/*!/film/* to sign paths starting with /tv/ or /film/ in any URL.
        Optional<String> pathGlobs = Optional.empty();
    
        // (Optional) A unique identifier for the session.
        Optional<String> sessionId = Optional.empty();
        // (Optional) Data payload to include in the token.
        Optional<String> data = Optional.empty();
        // (Optional) Header name and value to include in the signed token in name=value format.
        // May be specified more than once.
        // For example: [{'name': 'foo', 'value': 'bar'}, {'name': 'baz', 'value': 'qux'}]
        Optional<List<Header>> headers = Optional.empty();
        // (Optional) A list of comma-separated IP ranges. Both IPv4 and IPv6 ranges are acceptable.
        // For example: "203.0.113.0/24,2001:db8:4a7f:a732/64"
        Optional<String> ipRanges = Optional.empty();
    
        DualToken.signToken(
            base64Key,
            signatureAlgorithm,
            startTime,
            expiresTime,
            urlPrefix,
            fullPath,
            pathGlobs,
            sessionId,
            data,
            headers,
            ipRanges);
      }
    
      // Gets the signed URL suffix string for the Media CDN short token URL requests.
      // Result:
      //     The signed URL appended with the query parameters based on the
      // specified URL prefix and configuration.
      public static void signToken(
          byte[] base64Key, String signatureAlgorithm, Optional<Instant> startTime,
          Instant expirationTime, Optional<String> urlPrefix, Optional<String> fullPath,
          Optional<String> pathGlobs, Optional<String> sessionId, Optional<String> data,
          Optional<List<Header>> headers, Optional<String> ipRanges)
          throws NoSuchAlgorithmException, InvalidKeyException {
    
        String field = "";
        byte[] decodedKey = Base64.getUrlDecoder().decode(base64Key);
    
        // For most fields, the value in the token and the value to sign
        // are the same. Compared to the token, the FullPath and Headers
        // use a different string for the value to sign. To illustrate this difference,
        // we'll keep the token and the value to be signed separate.
        List<String> tokens = new ArrayList<>();
        List<String> toSign = new ArrayList<>();
    
        // Check for `fullPath` or `pathGlobs` or `urlPrefix`.
        if (fullPath.isPresent()) {
          tokens.add("FullPath");
          toSign.add(String.format("FullPath=%s", fullPath.get()));
        } else if (pathGlobs.isPresent()) {
          field = String.format("PathGlobs=%s", pathGlobs.get().trim());
          tokens.add(field);
          toSign.add(field);
        } else if (urlPrefix.isPresent()) {
          field = String.format("URLPrefix=%s",
              base64Encoder(urlPrefix.get().getBytes(StandardCharsets.UTF_8)));
          tokens.add(field);
          toSign.add(field);
        } else {
          throw new IllegalArgumentException(
              "User Input Missing: One of `urlPrefix`, `fullPath` or `pathGlobs` must be specified");
        }
    
        // Check & parse optional params.
        long epochDuration;
        if (startTime.isPresent()) {
          epochDuration = ChronoUnit.SECONDS.between(Instant.EPOCH, startTime.get());
          field = String.format("Starts=%s", epochDuration);
          tokens.add(field);
          toSign.add(field);
        }
    
        if (expirationTime == null) {
          expirationTime = Instant.now().plus(1, ChronoUnit.HOURS);
        }
        epochDuration = ChronoUnit.SECONDS.between(Instant.EPOCH, expirationTime);
        field = String.format("Expires=%s", epochDuration);
        tokens.add(field);
        toSign.add(field);
    
        if (sessionId.isPresent()) {
          field = String.format("SessionID=%s", sessionId.get());
          tokens.add(field);
          toSign.add(field);
        }
    
        if (data.isPresent()) {
          field = String.format("Data=%s", data.get());
          tokens.add(field);
          toSign.add(field);
        }
    
        if (headers.isPresent()) {
          List<String> headerNames = new ArrayList<>();
          List<String> headerPairs = new ArrayList<>();
    
          for (Header entry : headers.get()) {
            headerNames.add(entry.getName());
            headerPairs.add(String.format("%s=%s", entry.getName(), entry.getValue()));
          }
          tokens.add(String.format("Headers=%s", String.join(",", headerNames)));
          toSign.add(String.format("Headers=%s", String.join(",", headerPairs)));
        }
    
        if (ipRanges.isPresent()) {
          field = String.format("IPRanges=%s",
              base64Encoder(ipRanges.get().getBytes(StandardCharsets.US_ASCII)));
          tokens.add(field);
          toSign.add(field);
        }
    
        // Generate token.
        String toSignJoined = String.join("~", toSign);
        byte[] toSignBytes = toSignJoined.getBytes(StandardCharsets.UTF_8);
        String algorithm = signatureAlgorithm.toLowerCase();
    
        if (algorithm.equalsIgnoreCase("ed25519")) {
          Ed25519PrivateKeyParameters privateKey = new Ed25519PrivateKeyParameters(decodedKey, 0);
          Ed25519Signer signer = new Ed25519Signer();
          signer.init(true, privateKey);
          signer.update(toSignBytes, 0, toSignBytes.length);
          byte[] signature = signer.generateSignature();
          tokens.add(String.format("Signature=%s", base64Encoder(signature)));
        } else if (algorithm.equalsIgnoreCase("sha256")) {
          String sha256 = "HmacSHA256";
          Mac mac = Mac.getInstance(sha256);
          SecretKeySpec secretKeySpec = new SecretKeySpec(decodedKey, sha256);
          mac.init(secretKeySpec);
          byte[] signature = mac.doFinal(toSignBytes);
          tokens.add(String.format("hmac=%s", Hex.toHexString(signature)));
        } else if (algorithm.equalsIgnoreCase("sha1")) {
          String sha1 = "HmacSHA1";
          Mac mac = Mac.getInstance(sha1);
          SecretKeySpec secretKeySpec = new SecretKeySpec(decodedKey, sha1);
          mac.init(secretKeySpec);
          byte[] signature = mac.doFinal(toSignBytes);
          tokens.add(String.format("hmac=%s", Hex.toHexString(signature)));
        } else {
          throw new Error(
              "Input Missing Error: `signatureAlgorithm` can only be one of `sha1`, `sha256` or "
                  + "`ed25519`");
        }
        // The signed URL appended with the query parameters based on the
        // specified URL prefix and configuration.
        System.out.println(String.join("~", tokens));
      }
    
      // Returns a base64-encoded string compatible with Media CDN.
      // Media CDN uses URL-safe base64 encoding and strips off the padding at the
      // end.
      public static String base64Encoder(byte[] value) {
        byte[] encodedBytes = Base64.getUrlEncoder().withoutPadding().encode(value);
        return new String(encodedBytes, StandardCharsets.UTF_8);
      }
    
      public static class Header {
    
        private String name;
        private String value;
    
        public Header(String name, String value) {
          this.name = name;
          this.value = value;
        }
    
        public String getName() {
          return name;
        }
    
        public void setName(String name) {
          this.name = name;
        }
    
        public String getValue() {
          return value;
        }
    
        public void setValue(String value) {
          this.value = value;
        }
    
        @Override
        public String toString() {
          return "Header{"
              + "name='" + name + '\''
              + ", value='" + value + '\''
              + '}';
        }
      }
    
    }

The following sections describe the fields used by tokens.

## Required token fields

The following fields are required for every token:

  * `Expires`
  * One of any of the following: 
    * `PathGlobs`
    * `URLPrefix`
    * `FullPath`
  * One of either of the following: 
    * `Signature`
    * `hmac`



Unless otherwise specified, parameter names and their values are case-sensitive.

The following table explains each parameter:

Field name / aliases | Token parameters | Signed value  
---|---|---  
`Expires` `exp` | Integer seconds that have elapsed since the Unix epoch (1970-01-01T00:00:00Z) | `Expires=EXPIRATION_TIME`, after which the token is no longer valid.  
`PathGlobs` `paths`, `acl` | A list of up to five path segments to grant access to. The segments can be delimited by either commas (`,`) or exclamation marks (`!`) but not both. `PathGlobs` supports wildcarding in paths by using asterisks (`*`) and question marks (`?`). A single asterisk (`*`) character spans any number of path segments, unlike the pattern matching syntax for [`pathMatchTemplate`](https://docs.cloud.google.com/media-cdn/docs/routing#pattern-matching). Path parameters, denoted using semicolons (`;`), are not allowed because they create ambiguity while matching. For these reasons, ensure that your URL does not contain the following special characters: `,!*?;` | `PathGlobs=PATHS`  
`URLPrefix` |  A web-safe base64 encoded URL including the protocol `http://` or `https://` up to a point of your choosing. For example, some valid URLPrefix values for `https://example.com/foo/bar.ts` are `https://example.com`, `https://example.com/foo`, and `https://example.com/foo/bar`. | `URLPrefix=BASE_64_URL_PREFIX`  
`FullPath` | None. When specifying `FullPath` in a token, don't duplicate the path you specified in the signed value. In a token, include the field name without an `=`. | `FullPath=FULL_PATH_TO_OBJECT`  
`Signature` | A web-safe base64 encoded version of the signature. | Not applicable  
`hmac` | A web-safe base64 encoded version of the HMAC value. | Not applicable  
  
### `PathGlobs` wildcard syntax

The following table explains `PathGlobs` wildcard syntax.

Operator | Matches | Examples  
---|---|---  
`*` (asterisk) | Matches zero or more characters in the URL's path, including forward slash (`/`) characters.  | 

  * `/videos/*` matches any path that starts with `/videos/`.
  * `/videos/s*/4k/*` matches `/videos/s/4k/` and `/videos/s01/4k/main.m3u8`.
  * `/manifests/*/4k/*` matches `/manifests/s01/4k/main.m3u8` and `/manifests/s01/e01/4k/main.m3u8`. It doesn't match `/manifests/4k/main.m3u8`.

  
`?` (question mark) | Matches a single character in the URL's path, not including forward slash (`/`) characters.  | `/videos/s?main.m3u8` matches `/videos/s1main.m3u8`. It doesn't match either of `/videos/s01main.m3u8` or `/videos/s/main.m3u8`.   
  
Globs must start with either an asterisk (`*`) or a forward slash (`/`) for URL paths.

Because `*` and `/*` match all URL paths, we don't recommend using either in your signed tokens. For maximum protection, ensure that your globs match the content that you intend to grant access to.

## Optional token fields

Unless otherwise specified, parameter names and their values are case-sensitive.

The following table explains parameter names, any aliases, and details for optional parameters:

Field name / aliases | Parameters | Signed value  
---|---|---  
`Starts` `st` | Integer seconds since the Unix epoch (1970-01-01T00:00:00Z) | `Starts=START_TIME`  
`IPRanges` | A list of up to five IPv4 and IPv6 addresses in CIDR format for which this URL is valid in web-safe base64 format. For example, to specify the IP ranges "192.6.13.13/32,193.5.64.135/32", you specify `IPRanges=MTkyLjYuMTMuMTMvMzIsMTkzLjUuNjQuMTM1LzMy`. IPRanges may not be helpful to include in tokens when clients are at risk of WAN migrations or cases where the network path to your application frontend is different than the delivery path. Media CDN rejects clients with an `HTTP 403` code when they connect with an IP address that is not part of the signed request.  The following are cases that may result in Media CDN rejecting clients with an `HTTP 403` code: 

  * Dual-stack (IPv4, IPv6) environments
  * Connection migration (WiFi to cellular, and cellular to WiFi)
  * Mobile networks that use Carrier Gateway NAT (CGNAT or CGN)
  * Multi-path TCP (MPTCP)

All of these factors can contribute to a given client having a non-deterministic IP address during a video playback session. If the client IP address changes after you have issued access, and the client attempts to then download a video segment into their playback buffer, they receive an `HTTP 403` from Media CDN.  | `IPRanges=BASE_64_IP_RANGES`  
`SessionID` `id` | An arbitrary string, useful for logs analysis or playback tracing. To avoid creating an invalid token, use %-encoded or web-safe base64-encoded strings. The following characters must not be used for `SessionID`, as they cause the token to be invalid: "`~`", "`&`", or "` `" (space). | `SessionID=SESSION_ID_VALUE`  
`Data` `data`, `payload` | An arbitrary string, useful for logs analysis. To avoid creating an invalid token, use %-encoded or web-safe base64-encoded strings. The following characters must not be used for `Data`, as they cause the token to be invalid: "`~`", "`&`", or "` `" (space). | `data=DATA_VALUE`  
`Headers` | A comma-delimited list of header field names. Header names are case-insensitive for lookups in the request. Header names in the signed values are case-sensitive. If a header is missing, the value is the empty string. If there are multiple copies of a header, they're comma-concatenated. | `Headers=HEADER_1_NAME=HEADER_1_EXPECTED_VALUE, HEADER_2_NAME=HEADER_2_EXPECTED_VALUE`  
  
## Examples

The following sections show examples for generating tokens.

### Example using `FullPath`

Consider the following example using the `FullPath` field:

  * Item requested: `http://example.com/tv/my-show/s01/e01/playlist.m3u8`
  * Expiration time: 160000000



The signed value is:
    
    
    Expires=160000000~FullPath=/tv/my-show/s01/e01/playlist.m3u8
    

To create a token, sign the signed value with either an Ed25519 signature or a symmetric-key HMAC.

The following are example tokens created from a signed value:

### Ed25519 signature
    
    
    Expires=160000000~FullPath~Signature=SIGNATURE_OF_SIGNED_VALUE
    

Where SIGNATURE_OF_SIGNED_VALUE is the ED25519 signature of the signed value previously created.

### Symmetric-key HMAC
    
    
    Expires=160000000~FullPath~hmac=HMAC_OF_SIGNED_VALUE
    

Where HMAC_OF_SIGNED_VALUE is the symmetric-key HMAC of the signed value previously created.

In the preceding examples, `FullPath` is provided in the token, but the value isn't repeated from the path specified in the signed value. This lets you to sign the full path of the request without duplicating the request in the token.

### Example using `URLPrefix`

Consider the following example using the `URLPrefix` field:

  * Item requested: `http://example.com/tv/my-show/s01/e01/playlist.m3u8`
  * Expiration time: 160000000



The signed value is:
    
    
    Expires=160000000~URLPrefix=aHR0cDovL2V4YW1wbGUuY29tL3R2L215LXNob3cvczAxL2UwMS9wbGF5bGlzdC5tM3U4
    

In the preceding example, we replaced the path to the requested item, `http://example.com/tv/my-show/s01/e01/playlist.m3u8` with the path to the item in web-safe Base64 format, `aHR0cDovL2V4YW1wbGUuY29tL3R2L215LXNob3cvczAxL2UwMS9wbGF5bGlzdC5tM3U4`.

To create a token, sign the signed value with either an Ed25519 signature or a symmetric-key HMAC.

The following are example tokens created from a signed value:

### Ed25519 signature
    
    
    Expires=160000000~URLPrefix=aHR0cDovL2V4YW1wbGUuY29tL3R2L215LXNob3cvczAxL2UwMS9wbGF5bGlzdC5tM3U4~Signature=SIGNATURE_OF_SIGNED_VALUE
    

Where SIGNATURE_OF_SIGNED_VALUE is the ED25519 signature of the signed value previously created.

### Symmetric-key HMAC
    
    
    Expires=160000000~URLPrefix=aHR0cDovL2V4YW1wbGUuY29tL3R2L215LXNob3cvczAxL2UwMS9wbGF5bGlzdC5tM3U4~hmac=HMAC_OF_SIGNED_VALUE
    

Where HMAC_OF_SIGNED_VALUE is the symmetric-key HMAC of the signed value previously created.

### Example using `Headers`

Consider the following example using the `Headers` field:

  * Item requested: `http://example.com/tv/my-show/s01/e01/playlist.m3u8`
  * Expiration time: 160000000
  * PathGlobs value: `*`
  * Expected request headers: 
    * `user-agent: browser`
    * `accept: text/html`



The signed value is:
    
    
    Expires=160000000~PathGlobs=*~Headers=user-agent=browser,accept=text/html
    

To create a token, sign the signed value with either an Ed25519 signature or a symmetric-key HMAC.

The following are example tokens created from a signed value:

### Ed25519 signature
    
    
    Expires=160000000~PathGlobs=*~Headers=user-agent,accept~Signature=SIGNATURE_OF_SIGNED_VALUE
    

Where SIGNATURE_OF_SIGNED_VALUE is the ED25519 signature of the signed value previously created.

### Symmetric-key HMAC
    
    
    Expires=160000000~PathGlobs=*~Headers=user-agent,accept~hmac=HMAC_OF_SIGNED_VALUE
    

Where HMAC_OF_SIGNED_VALUE is the symmetric-key HMAC of the signed value previously created.

In the preceding examples, `Headers=user-agent,accept` is provided in the token, but the expected header values aren't repeated from the signed value. This lets you sign specific request header key-value pairs without duplicating the values in the token.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
