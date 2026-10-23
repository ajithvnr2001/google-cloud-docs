---
url: https://docs.cloud.google.com/media-cdn/docs/generate-signatures/
title: Generate signatures \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:55.910350+00:00
---

# Generate signatures  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/generate-signatures/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Generate signatures Stay organized with collections  Save and categorize content based on your preferences. 

This guide explains how to create a signature, and the required and optional fields for signatures.

To create a signature, you compose a string to sign, which we refer to as a _signed value_ in this guide. The signed value includes parameters that describe the content you are protecting, the expiration time of the signed value, and so forth.

You use the signed value while creating a signature string. You create a signature string by composing the parameters for the signature, such as an asymmetric-key Ed25519 signature of the signed value.

Media CDN uses the final composed signature to help protect your content.

### Supported signing formats

Media CDN supports the following signed request formats.

Format | Behavior | Example  
---|---|---  
**Query parameters (exact URL)** |  Exact URL, for granting access to a specific URL. | Exact: `https://media.example.com/content/manifest.m3u8?  
Expires=EXPIRATION  
&KeyName=KEY_NAME  
&Signature=SIGNATURE`  
**Query parameters (URL prefix)** |  Specifying a `URLPrefix` lets you sign a prefix and append the same query parameters to multiple URLs within your player or manifest generation.  |  What to sign: `URLPrefix=PREFIX  
&Expires=EXPIRATION  
&KeyName=KEY_NAME  
&Signature=SIGNATURE` Replace `PREFIX` with the prefix to grant access to, including the scheme, host, and partial path.   
**Path component** |  Prefix: allows access to any URL with a prefix prior to the `"/edge-cache-token=[...]"` component. This allows relative manifest URLs to automatically inherit the signed URL component when fetching sub-resources. |  `https://media.example.com/video/edge-cache-token=Expires=EXPIRATION  
&KeyName=KEY_NAME  
&Signature=SIGNATURE/manifest_12382131.m3u8`  
**Signed cookie** | Prefix: the cookie allows access to any URL with the prefix specified in the signed `URLPrefix` value.  | Edge-Cache-Cookie: `URLPrefix=PREFIX:  
Expires=EXPIRATION:  
KeyName=KEY_NAME:  
Signature=SIGNATURE`  
  
## Create a signature

**Note:** The host and path components of the URL (or URLPrefix) are used to validate signatures. When you provide a URL to any of these programmatic APIs, omit the port. In other words, for a path like `https://example.com:443/path`, specify the path as `https://example.com/path`.

  1. Create a signed value by concatenating a string that contains the required signature fields and desired optional signature fields.

If specified, `URLPrefix` must come first, followed by `Expires`, `KeyName`, and then any optional parameters.

Separate each field and any parameters with the following:

     * For cookies, use a colon `:` character.
     * For query parameters and path components, use an ampersand `&` character.
  2. Sign the signed value with an Ed25519 signature.

  3. Append a field separator (either `:` or `&`) followed by `Signature=` and the Ed25519 signature to the end of the string.




### Create a signed URL

The following code samples shows how to programmatically create a signed URL.

### Go

To authenticate to Media CDN, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"crypto/ed25519"
    	"encoding/base64"
    	"fmt"
    	"io"
    	"strings"
    	"time"
    )
    
    // signURL prints the signed URL string for the specified URL and configuration.
    func signURL(w io.Writer, url, keyName string, privateKey []byte, expires time.Time) error {
    	// url := "http://example.com"
    	// keyName := "your_key_name"
    	// privateKey := "[]byte{34, 31, ...}"
    	// expires := time.Unix(1558131350, 0)
    
    	sep := '?'
    	if strings.ContainsRune(url, '?') {
    		sep = '&'
    	}
    	toSign := fmt.Sprintf("%s%cExpires=%d&KeyName=%s", url, sep, expires.Unix(), keyName)
    	sig := ed25519.Sign(privateKey, []byte(toSign))
    
    	fmt.Fprintf(w, "%s&Signature=%s", toSign, base64.RawURLEncoding.EncodeToString(sig))
    
    	return nil
    }
    

### Python

To authenticate to Media CDN, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import base64
    import datetime
    
    import cryptography.hazmat.primitives.asymmetric.ed25519 as ed25519
    
    
    from six.moves import urllib
    
    def sign_url(
        url: str, key_name: str, base64_key: str, expiration_time: datetime.datetime
    ) -> str:
        """Gets the Signed URL string for the specified URL and configuration.
    
        Args:
            url: URL to sign as a string.
            key_name: name of the signing key as a string.
            base64_key: signing key as a base64 encoded byte string.
            expiration_time: expiration time as a UTC datetime object.
    
        Returns:
            Returns the Signed URL appended with the query parameters based on the
            specified configuration.
        """
        stripped_url = url.strip()
        parsed_url = urllib.parse.urlsplit(stripped_url)
        query_params = urllib.parse.parse_qs(parsed_url.query, keep_blank_values=True)
        epoch = datetime.datetime.utcfromtimestamp(0)
        expiration_timestamp = int((expiration_time - epoch).total_seconds())
        decoded_key = base64.urlsafe_b64decode(base64_key)
    
        url_pattern = "{url}{separator}Expires={expires}&KeyName={key_name}"
    
        url_to_sign = url_pattern.format(
            url=stripped_url,
            separator="&" if query_params else "?",
            expires=expiration_timestamp,
            key_name=key_name,
        )
    
        digest = ed25519.Ed25519PrivateKey.from_private_bytes(decoded_key).sign(
            url_to_sign.encode("utf-8")
        )
        signature = base64.urlsafe_b64encode(digest).decode("utf-8")
        signed_url = "{url}&Signature={signature}".format(
            url=url_to_sign, signature=signature
        )
    
        return signed_url
    
    

### Create a signed URL prefix

The following code samples show how to programmatically create a signed URL prefix.

### Go

To authenticate to Media CDN, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"crypto/ed25519"
    	"encoding/base64"
    	"fmt"
    	"io"
    	"strings"
    	"time"
    )
    
    // signURLPrefix prints the signed URL string for the specified URL prefix and configuration.
    func signURLPrefix(w io.Writer, urlPrefix, keyName string, privateKey []byte, expires time.Time) error {
    	// urlPrefix := "https://examples.com"
    	// keyName := "your_key_name"
    	// privateKey := "[]byte{34, 31, ...}"
    	// expires := time.Unix(1558131350, 0)
    
    	sep := '?'
    	if strings.ContainsRune(urlPrefix, '?') {
    		sep = '&'
    	}
    
    	toSign := fmt.Sprintf(
    		"URLPrefix=%s&Expires=%d&KeyName=%s",
    		base64.RawURLEncoding.EncodeToString([]byte(urlPrefix)),
    		expires.Unix(),
    		keyName,
    	)
    	sig := ed25519.Sign(privateKey, []byte(toSign))
    
    	fmt.Fprintf(
    		w,
    		"%s%c%s&Signature=%s",
    		urlPrefix,
    		sep,
    		toSign,
    		base64.RawURLEncoding.EncodeToString(sig),
    	)
    
    	return nil
    }
    

### Python

To authenticate to Media CDN, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import base64
    import datetime
    
    import cryptography.hazmat.primitives.asymmetric.ed25519 as ed25519
    
    
    from six.moves import urllib
    
    def sign_url_prefix(
        url: str,
        url_prefix: str,
        key_name: str,
        base64_key: str,
        expiration_time: datetime.datetime,
    ) -> str:
        """Gets the Signed URL string for the specified URL prefix and configuration.
    
        Args:
            url: URL of request.
            url_prefix: URL prefix to sign as a string.
            key_name: name of the signing key as a string.
            base64_key: signing key as a base64 encoded string.
            expiration_time: expiration time as a UTC datetime object.
    
        Returns:
            Returns the Signed URL appended with the query parameters based on the
            specified URL prefix and configuration.
        """
        stripped_url = url.strip()
        parsed_url = urllib.parse.urlsplit(stripped_url)
        query_params = urllib.parse.parse_qs(parsed_url.query, keep_blank_values=True)
        encoded_url_prefix = base64.urlsafe_b64encode(
            url_prefix.strip().encode("utf-8")
        ).decode("utf-8")
        epoch = datetime.datetime.utcfromtimestamp(0)
        expiration_timestamp = int((expiration_time - epoch).total_seconds())
        decoded_key = base64.urlsafe_b64decode(base64_key)
    
        policy_pattern = (
            "URLPrefix={encoded_url_prefix}&Expires={expires}&KeyName={key_name}"
        )
        policy = policy_pattern.format(
            encoded_url_prefix=encoded_url_prefix,
            expires=expiration_timestamp,
            key_name=key_name,
        )
    
        digest = ed25519.Ed25519PrivateKey.from_private_bytes(decoded_key).sign(
            policy.encode("utf-8")
        )
        signature = base64.urlsafe_b64encode(digest).decode("utf-8")
        signed_url = "{url}{separator}{policy}&Signature={signature}".format(
            url=stripped_url,
            separator="&" if query_params else "?",
            policy=policy,
            signature=signature,
        )
        return signed_url
    
    

### Create a signed URL cookie

The following code samples show how to programmatically create a signed URL cookie.

### Go

To authenticate to Media CDN, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"crypto/ed25519"
    	"encoding/base64"
    	"fmt"
    	"io"
    	"time"
    )
    
    // signCookie prints the signed cookie value for the specified URL prefix and configuration.
    func signCookie(w io.Writer, urlPrefix, keyName string, privateKey []byte, expires time.Time) error {
    	// urlPrefix := "http://example.com"
    	// keyName := "your_key_name"
    	// privateKey := "[]byte{34, 31, ...}"
    	// expires := time.Unix(1558131350, 0)
    
    	toSign := fmt.Sprintf(
    		"URLPrefix=%s:Expires=%d:KeyName=%s",
    		base64.RawURLEncoding.EncodeToString([]byte(urlPrefix)),
    		expires.Unix(),
    		keyName,
    	)
    	sig := ed25519.Sign(privateKey, []byte(toSign))
    
    	fmt.Fprintf(
    		w,
    		"Edge-Cache-Cookie=%s:Signature=%s",
    		toSign,
    		base64.RawURLEncoding.EncodeToString(sig),
    	)
    
    	return nil
    }
    

### Python

To authenticate to Media CDN, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import base64
    import datetime
    
    import cryptography.hazmat.primitives.asymmetric.ed25519 as ed25519
    
    
    from six.moves import urllib
    
    def sign_cookie(
        url_prefix: str, key_name: str, base64_key: str, expiration_time: datetime.datetime
    ) -> str:
        """Gets the Signed cookie value for the specified URL prefix and configuration.
    
        Args:
            url_prefix: URL prefix to sign as a string.
            key_name: name of the signing key as a string.
            base64_key: signing key as a base64 encoded string.
            expiration_time: expiration time as a UTC datetime object.
    
        Returns:
            Returns the Edge-Cache-Cookie value based on the specified configuration.
        """
        encoded_url_prefix = base64.urlsafe_b64encode(
            url_prefix.strip().encode("utf-8")
        ).decode("utf-8")
        epoch = datetime.datetime.utcfromtimestamp(0)
        expiration_timestamp = int((expiration_time - epoch).total_seconds())
        decoded_key = base64.urlsafe_b64decode(base64_key)
    
        policy_pattern = (
            "URLPrefix={encoded_url_prefix}:Expires={expires}:KeyName={key_name}"
        )
        policy = policy_pattern.format(
            encoded_url_prefix=encoded_url_prefix,
            expires=expiration_timestamp,
            key_name=key_name,
        )
    
        digest = ed25519.Ed25519PrivateKey.from_private_bytes(decoded_key).sign(
            policy.encode("utf-8")
        )
        signature = base64.urlsafe_b64encode(digest).decode("utf-8")
    
        signed_policy = "Edge-Cache-Cookie={policy}:Signature={signature}".format(
            policy=policy, signature=signature
        )
        return signed_policy
    
    

### Create a signed path component

The following code samples show how to programmatically create a signed path component.

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
    
    
    def sign_path_component(
        url_prefix: str,
        filename: str,
        key_name: str,
        base64_key: str,
        expiration_time: datetime.datetime,
    ) -> str:
        """Gets the Signed URL string for the specified URL prefix and configuration.
    
        Args:
            url_prefix: URL Prefix to sign as a string.
            filename: The filename of the sample request
            key_name: The name of the signing key as a string.
            base64_key: The signing key as a base64 encoded string.
            expiration_time: Expiration time as a UTC datetime object with timezone.
    
        Returns:
            Returns the Signed URL appended with the query parameters based on the
            specified URL prefix and configuration.
        """
    
        expiration_duration = expiration_time.astimezone(
            tz=datetime.timezone.utc
        ) - datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
        decoded_key = base64.urlsafe_b64decode(base64_key)
    
        policy_pattern = "{url_prefix}edge-cache-token=Expires={expires}&KeyName={key_name}"
        policy = policy_pattern.format(
            url_prefix=url_prefix,
            expires=int(expiration_duration.total_seconds()),
            key_name=key_name,
        )
    
        digest = ed25519.Ed25519PrivateKey.from_private_bytes(decoded_key).sign(
            policy.encode("utf-8")
        )
        signature = base64_encoder(digest)
    
        signed_url = "{policy}&Signature={signature}/{filename}".format(
            policy=policy, signature=signature, filename=filename
        )
    
        return signed_url
    
    

## Required signature fields

The following fields are required for every signature:

  * `Expires`
  * `KeyName`
  * `Signature`



If query parameters are present, they must be grouped together as the last parameters in the URL. Unless otherwise specified, parameter names and their values are case-sensitive.

The following table explains each parameter:

Field name | Signature parameters | Signed value  
---|---|---  
`Expires` | Integer seconds that have elapsed since the Unix epoch (1970-01-01T00:00:00Z) | `Expires=EXPIRATION_TIME`, after which the signature is no longer valid.  
`KeyName` | The name of the `EdgeCacheKeyset` used to sign this request. `KeyName` refers to the entire keyset, not individual keys within the keyset itself.  | `KeyName=EDGE_CACHE_KEYSET`  
`Signature` | A base-64 encoded version of the signature. | Not applicable  
  
## Optional signature fields

If query parameters are present, they must be grouped together as the last parameters in the URL. Unless otherwise specified, parameter names and their values are case-sensitive.

The following table explains each parameter's name and detail for optional signature parameters:

Field name | Signature parameters | Signed value  
---|---|---  
**`HeaderName`** | A named request header field name that must be present in the request. Must be lowercase when signed because header field names are case-sensitive. Media CDN lowercases the header before validating the signature. | `HeaderName=HEADER_NAME`  
**`HeaderValue`** | A named request header field value that must be present in the request. This is commonly a user ID or other opaque identifier. Requests with `HeaderValue` but without `HeaderName` are rejected.  | `HeaderValue=HEADER_VALUE`  
`IPRanges` | A list of up to five IPv4 and IPv6 addresses in CIDR format for which this URL is valid in web-safe base64 format. For example, to specify the IP ranges "192.6.13.13/32,193.5.64.135/32", you specify `IPRanges=MTkyLjYuMTMuMTMvMzIsMTkzLjUuNjQuMTM1LzMy`. IPRanges may not be helpful to include in signatures when clients are at risk of WAN migrations or cases where the network path to your application frontend is different than the delivery path. Media CDN rejects clients with an `HTTP 403` code when they connect with an IP address that is not part of the signed request.  The following are cases that may result in Media CDN rejecting clients with an `HTTP 403` code: 

  * Dual-stack (IPv4, IPv6) environments
  * Connection migration (WiFi to cellular, and cellular to WiFi)
  * Mobile networks that use Carrier Gateway NAT (CGNAT or CGN)
  * Multi-path TCP (MPTCP)

All of these factors can contribute to a given client having a non-deterministic IP address during a video playback session. If the client IP address changes after you have issued access, and the client attempts to then download a video segment into their playback buffer, they receive an `HTTP 403` from Media CDN.  | `IPRanges=BASE_64_IP_RANGES`  
**`URLPrefix`** | The base64 (URL-safe) URL prefix to grant access to. Specifying a `URLPrefix` lets you sign a prefix and append the same query parameters to multiple URLs within your player or manifest generation. The `URLPrefix` is required when using the signed cookie format.  | `URLPrefix=BASE_64_URL_PREFIX`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
