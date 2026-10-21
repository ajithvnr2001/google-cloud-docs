---
url: https://docs.cloud.google.com/web-risk/docs/samples/webrisk-compute-threatlist-diff/
title: Get threat list diff \u00a0|\u00a0 Web Risk \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:30:17.849243+00:00
---

# Get threat list diff  |  Web Risk  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/web-risk/docs/samples/webrisk-compute-threatlist-diff/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Web Risk ](https://docs.cloud.google.com/web-risk/docs)
  * [ Samples ](https://docs.cloud.google.com/web-risk/docs/samples)



#  Get threat list diff Stay organized with collections  Save and categorize content based on your preferences. 

Get the diff of a threat list since last update

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Using the Update API](https://docs.cloud.google.com/web-risk/docs/update-api)



## Code sample

### Java

To authenticate to Web Risk, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.webrisk.v1.[WebRiskServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.cloud.webrisk.v1.WebRiskServiceClient.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.webrisk.v1.[CompressionType](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.CompressionType.html);
    import com.google.webrisk.v1.[ComputeThreatListDiffRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ComputeThreatListDiffRequest.html);
    import com.google.webrisk.v1.[ComputeThreatListDiffRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ComputeThreatListDiffRequest.html).[Constraints](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ComputeThreatListDiffRequest.Constraints.html);
    import com.google.webrisk.v1.[ComputeThreatListDiffResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ComputeThreatListDiffResponse.html);
    import com.google.webrisk.v1.[ThreatType](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatType.html);
    import java.io.IOException;
    
    public class ComputeThreatListDiff {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // The threat list to update. Only a single ThreatType should be specified per request.
        [ThreatType](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatType.html) threatType = [ThreatType](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatType.html).MALWARE;
    
        // The current version token of the client for the requested list. If the client does not have
        // a version token (this is the first time calling ComputeThreatListDiff), this may be
        // left empty and a full database snapshot will be returned.
        [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) versionToken = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).EMPTY;
    
        // The maximum size in number of entries. The diff will not contain more entries
        // than this value. This should be a power of 2 between 2**10 and 2**20.
        // If zero, no diff size limit is set.
        int maxDiffEntries = 1024;
    
        // Sets the maximum number of entries that the client is willing to have in the local database.
        // This should be a power of 2 between 2**10 and 2**20. If zero, no database size limit is set.
        int maxDatabaseEntries = 1024;
    
        // The compression type supported by the client.
        [CompressionType](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.CompressionType.html) compressionType = [CompressionType](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.CompressionType.html).RAW;
    
        computeThreatDiffList(threatType, versionToken, maxDiffEntries, maxDatabaseEntries,
            compressionType);
      }
    
      // Gets the most recent threat list diffs. These diffs should be applied to a local database of
      // hashes to keep it up-to-date.
      // If the local database is empty or excessively out-of-date,
      // a complete snapshot of the database will be returned. This Method only updates a
      // single ThreatList at a time. To update multiple ThreatList databases, this method needs to be
      // called once for each list.
      public static void computeThreatDiffList([ThreatType](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatType.html) threatType, [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) versionToken,
          int maxDiffEntries, int maxDatabaseEntries, [CompressionType](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.CompressionType.html) compressionType)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `webRiskServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([WebRiskServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.cloud.webrisk.v1.WebRiskServiceClient.html) webRiskServiceClient = [WebRiskServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.cloud.webrisk.v1.WebRiskServiceClient.html).create()) {
    
          [Constraints](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ComputeThreatListDiffRequest.Constraints.html) constraints = [Constraints](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ComputeThreatListDiffRequest.Constraints.html).newBuilder()
              .[setMaxDiffEntries](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ComputeThreatListDiffRequest.Constraints.Builder.html#com_google_webrisk_v1_ComputeThreatListDiffRequest_Constraints_Builder_setMaxDiffEntries_int_)(maxDiffEntries)
              .[setMaxDatabaseEntries](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ComputeThreatListDiffRequest.Constraints.Builder.html#com_google_webrisk_v1_ComputeThreatListDiffRequest_Constraints_Builder_setMaxDatabaseEntries_int_)(maxDatabaseEntries)
              .[addSupportedCompressions](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ComputeThreatListDiffRequest.Constraints.Builder.html#com_google_webrisk_v1_ComputeThreatListDiffRequest_Constraints_Builder_addSupportedCompressions_com_google_webrisk_v1_CompressionType_)(compressionType)
              .build();
    
          [ComputeThreatListDiffResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ComputeThreatListDiffResponse.html) response = webRiskServiceClient.computeThreatListDiff(
              [ComputeThreatListDiffRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ComputeThreatListDiffRequest.html).newBuilder()
                  .[setThreatType](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ComputeThreatListDiffRequest.Builder.html#com_google_webrisk_v1_ComputeThreatListDiffRequest_Builder_setThreatType_com_google_webrisk_v1_ThreatType_)(threatType)
                  .[setVersionToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ComputeThreatListDiffRequest.Builder.html#com_google_webrisk_v1_ComputeThreatListDiffRequest_Builder_setVersionToken_com_google_protobuf_ByteString_)(versionToken)
                  .[setConstraints](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ComputeThreatListDiffRequest.Builder.html#com_google_webrisk_v1_ComputeThreatListDiffRequest_Builder_setConstraints_com_google_webrisk_v1_ComputeThreatListDiffRequest_Constraints_)(constraints)
                  .build());
    
          // The returned response contains the following information:
          // https://cloud.google.com/web-risk/docs/reference/rpc/google.cloud.webrisk.v1#computethreatlistdiffresponse
          // Type of response: DIFF/ RESET/ RESPONSE_TYPE_UNSPECIFIED
          System.out.println(response.[getResponseType](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ComputeThreatListDiffResponse.html#com_google_webrisk_v1_ComputeThreatListDiffResponse_getResponseType__)());
          // List of entries to add and/or remove.
          // System.out.println(response.getAdditions());
          // System.out.println(response.getRemovals());
    
          // New version token to be used the next time when querying.
          System.out.println(response.[getNewVersionToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ComputeThreatListDiffResponse.html#com_google_webrisk_v1_ComputeThreatListDiffResponse_getNewVersionToken__)());
    
          // Recommended next diff timestamp.
          System.out.println(response.[getRecommendedNextDiff](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ComputeThreatListDiffResponse.html#com_google_webrisk_v1_ComputeThreatListDiffResponse_getRecommendedNextDiff__)());
    
          System.out.println("Obtained threat list diff.");
        }
      }
    }

### Python

To authenticate to Web Risk, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest)
    from google.cloud.webrisk_v1 import [ComputeThreatListDiffResponse](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.ComputeThreatListDiffResponse.html)
    
    
    def compute_threatlist_diff(
        threat_type: [webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest).[ThreatType](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.ThreatType.html),
        version_token: bytes,
        max_diff_entries: int,
        max_database_entries: int,
        compression_type: [webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest).[CompressionType](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.CompressionType.html),
    ) -> ComputeThreatListDiffResponse:
        """Gets the most recent threat list diffs.
    
        These diffs should be applied to a local database of hashes to keep it up-to-date.
        If the local database is empty or excessively out-of-date,
        a complete snapshot of the database will be returned. This Method only updates a
        single ThreatList at a time. To update multiple ThreatList databases, this method needs to be
        called once for each list.
    
        Args:
            threat_type: The threat list to update. Only a single ThreatType should be specified per request.
                threat_type = webrisk_v1.ThreatType.MALWARE
    
            version_token: The current version token of the client for the requested list. If the
                client does not have a version token (this is the first time calling ComputeThreatListDiff),
                this may be left empty and a full database snapshot will be returned.
    
            max_diff_entries: The maximum size in number of entries. The diff will not contain more entries
                than this value. This should be a power of 2 between 2**10 and 2**20.
                If zero, no diff size limit is set.
                max_diff_entries = 1024
    
            max_database_entries: Sets the maximum number of entries that the client is willing to have in the local database.
                This should be a power of 2 between 2**10 and 2**20. If zero, no database size limit is set.
                max_database_entries = 1024
    
            compression_type: The compression type supported by the client.
                compression_type = webrisk_v1.CompressionType.RAW
    
        Returns:
            The response which contains the diff between local and remote threat lists. In addition to the threat list,
            the response also contains the version token and the recommended time for next diff.
        """
    
        webrisk_client = [webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest).[WebRiskServiceClient](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.services.web_risk_service.WebRiskServiceClient.html)()
    
        constraints = [webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest).[ComputeThreatListDiffRequest](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.ComputeThreatListDiffRequest.html).[Constraints](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.ComputeThreatListDiffRequest.Constraints.html)()
        constraints.max_diff_entries = max_diff_entries
        constraints.max_database_entries = max_database_entries
        constraints.supported_compressions = [compression_type]
    
        request = [webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest).[ComputeThreatListDiffRequest](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.ComputeThreatListDiffRequest.html)()
        request.threat_type = threat_type
        request.version_token = version_token
        request.constraints = constraints
    
        response = webrisk_client.[compute_threat_list_diff](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.services.web_risk_service.WebRiskServiceClient.html#google_cloud_webrisk_v1_services_web_risk_service_WebRiskServiceClient_compute_threat_list_diff)(request)
    
        # The returned response contains the following information:
        # https://cloud.google.com/web-risk/docs/reference/rpc/google.cloud.webrisk.v1#computethreatlistdiffresponse
        # Type of response: DIFF/ RESET/ RESPONSE_TYPE_UNSPECIFIED
        print(response.response_type)
        # New version token to be used the next time when querying.
        print(response.new_version_token)
        # Recommended next diff timestamp.
        print(response.recommended_next_diff)
    
        return response
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=webrisk). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
