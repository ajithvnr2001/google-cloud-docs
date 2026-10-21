---
url: https://docs.cloud.google.com/web-risk/docs/samples/webrisk-search-hash/
title: Search a hash \u00a0|\u00a0 Web Risk \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:30:17.900666+00:00
---

# Search a hash  |  Web Risk  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/web-risk/docs/samples/webrisk-search-hash/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Web Risk ](https://docs.cloud.google.com/web-risk/docs)
  * [ Samples ](https://docs.cloud.google.com/web-risk/docs/samples)



#  Search a hash Stay organized with collections  Save and categorize content based on your preferences. 

Create a Webrisk client and search for a hash

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Using the Update API](https://docs.cloud.google.com/web-risk/docs/update-api)



## Code sample

### Java

To authenticate to Web Risk, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.webrisk.v1.[WebRiskServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.cloud.webrisk.v1.WebRiskServiceClient.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.webrisk.v1.[SearchHashesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.SearchHashesRequest.html);
    import com.google.webrisk.v1.[SearchHashesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.SearchHashesResponse.html);
    import com.google.webrisk.v1.[SearchHashesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.SearchHashesResponse.html).[ThreatHash](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.SearchHashesResponse.ThreatHash.html);
    import com.google.webrisk.v1.[ThreatType](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatType.html);
    import java.io.IOException;
    import java.nio.charset.StandardCharsets;
    import java.security.MessageDigest;
    import java.security.NoSuchAlgorithmException;
    import java.util.Arrays;
    import java.util.Base64;
    import java.util.List;
    
    public class SearchHashes {
    
      public static void main(String[] args) throws IOException, NoSuchAlgorithmException {
        // TODO(developer): Replace these variables before running the sample.
        // A hash prefix, consisting of the most significant 4-32 bytes of a SHA256 hash.
        // For JSON requests, this field is base64-encoded. Note that if this parameter is provided
        // by a URI, it must be encoded using the web safe base64 variant (RFC 4648).
        String uri = "http://example.com";
        String encodedUri = Base64.getUrlEncoder().encodeToString(uri.getBytes(StandardCharsets.UTF_8));
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        byte[] encodedHashPrefix = digest.digest(encodedUri.getBytes(StandardCharsets.UTF_8));
    
        // The ThreatLists to search in. Multiple ThreatLists may be specified.
        // For the list on threat types, see: https://cloud.google.com/web-risk/docs/reference/rpc/google.cloud.webrisk.v1#threattype
        List<ThreatType> threatTypes = Arrays.asList([ThreatType](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatType.html).MALWARE, [ThreatType](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatType.html).SOCIAL_ENGINEERING);
    
        searchHash([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(encodedHashPrefix), threatTypes);
      }
    
      // Gets the full hashes that match the requested hash prefix.
      // This is used after a hash prefix is looked up in a threatList and there is a match.
      // The client side threatList only holds partial hashes so the client must query this method
      // to determine if there is a full hash match of a threat.
      public static void searchHash([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) encodedHashPrefix, List<ThreatType> threatTypes)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `webRiskServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([WebRiskServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.cloud.webrisk.v1.WebRiskServiceClient.html) webRiskServiceClient = [WebRiskServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.cloud.webrisk.v1.WebRiskServiceClient.html).create()) {
    
          // Set the hashPrefix and the threat types to search in.
          [SearchHashesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.SearchHashesResponse.html) response = webRiskServiceClient.searchHashes(
              [SearchHashesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.SearchHashesRequest.html).newBuilder()
                  .[setHashPrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.SearchHashesRequest.Builder.html#com_google_webrisk_v1_SearchHashesRequest_Builder_setHashPrefix_com_google_protobuf_ByteString_)(encodedHashPrefix)
                  .addAllThreatTypes(threatTypes)
                  .build());
    
          // Get all the hashes that match the prefix. Cache the returned hashes until the time
          // specified in threatHash.getExpireTime()
          // For more information on response type, see: https://cloud.google.com/web-risk/docs/reference/rpc/google.cloud.webrisk.v1#threathash
          for ([ThreatHash](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.SearchHashesResponse.ThreatHash.html) threatHash : response.[getThreatsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.SearchHashesResponse.html#com_google_webrisk_v1_SearchHashesResponse_getThreatsList__)()) {
            System.out.println(threatHash.getHash());
          }
          System.out.println("Completed searching threat hashes.");
        }
      }
    }

### Python

To authenticate to Web Risk, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest)
    
    
    def search_hashes(hash_prefix: bytes, threat_type: [webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest).[ThreatType](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.ThreatType.html)) -> list:
        """Gets the full hashes that match the requested hash prefix.
    
        This is used after a hash prefix is looked up in a threatList and there is a match.
        The client side threatList only holds partial hashes so the client must query this method
        to determine if there is a full hash match of a threat.
    
        Args:
            hash_prefix: A hash prefix, consisting of the most significant 4-32 bytes of a SHA256 hash.
                For JSON requests, this field is base64-encoded. Note that if this parameter is provided
                by a URI, it must be encoded using the web safe base64 variant (RFC 4648).
                Example:
                    uri = "http://example.com"
                    sha256 = sha256()
                    sha256.update(base64.urlsafe_b64encode(bytes(uri, "utf-8")))
                    hex_string = sha256.digest()
    
            threat_type: The ThreatLists to search in. Multiple ThreatLists may be specified.
                For the list on threat types, see:
                https://cloud.google.com/web-risk/docs/reference/rpc/google.cloud.webrisk.v1#threattype
                threat_type = [webrisk_v1.ThreatType.MALWARE, webrisk_v1.ThreatType.SOCIAL_ENGINEERING]
    
        Returns:
            A hash list that contain all hashes that matches the given hash prefix.
        """
        webrisk_client = [webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest).[WebRiskServiceClient](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.services.web_risk_service.WebRiskServiceClient.html)()
    
        # Set the hashPrefix and the threat types to search in.
        request = [webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest).[SearchHashesRequest](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.SearchHashesRequest.html)()
        request.hash_prefix = hash_prefix
        request.threat_types = [threat_type]
    
        response = webrisk_client.[search_hashes](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.services.web_risk_service.WebRiskServiceClient.html#google_cloud_webrisk_v1_services_web_risk_service_WebRiskServiceClient_search_hashes)(request)
    
        # Get all the hashes that match the prefix. Cache the returned hashes until the time
        # specified in threat_hash.expire_time
        # For more information on response type, see:
        # https://cloud.google.com/web-risk/docs/reference/rpc/google.cloud.webrisk.v1#threathash
        hash_list = []
        for threat_hash in response.threats:
            hash_list.append(threat_hash.hash)
        return hash_list
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=webrisk). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
