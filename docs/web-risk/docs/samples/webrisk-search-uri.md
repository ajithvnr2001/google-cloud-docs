---
url: https://docs.cloud.google.com/web-risk/docs/samples/webrisk-search-uri/
title: Search a URI \u00a0|\u00a0 Web Risk \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:30:17.735933+00:00
---

# Search a URI  |  Web Risk  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/web-risk/docs/samples/webrisk-search-uri/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Web Risk ](https://docs.cloud.google.com/web-risk/docs)
  * [ Samples ](https://docs.cloud.google.com/web-risk/docs/samples)



#  Search a URI Stay organized with collections  Save and categorize content based on your preferences. 

Create a Webrisk client and search for a URI.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Using the Lookup API](https://docs.cloud.google.com/web-risk/docs/lookup-api)



## Code sample

### Java

To authenticate to Web Risk, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.webrisk.v1.[WebRiskServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.cloud.webrisk.v1.WebRiskServiceClient.html);
    import com.google.webrisk.v1.[SearchUrisRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.SearchUrisRequest.html);
    import com.google.webrisk.v1.[SearchUrisResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.SearchUrisResponse.html);
    import com.google.webrisk.v1.[ThreatType](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatType.html);
    import java.io.IOException;
    
    public class SearchUri {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // The URI to be checked for matches.
        String uri = "http://testsafebrowsing.appspot.com/s/malware.html";
    
        // The ThreatLists to search in. Multiple ThreatLists may be specified.
        [ThreatType](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatType.html) threatType = [ThreatType](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatType.html).MALWARE;
    
        searchUri(uri, threatType);
      }
    
      // This method is used to check whether a URI is on a given threatList. Multiple threatLists may
      // be searched in a single query.
      // The response will list all requested threatLists the URI was found to match. If the URI is not
      // found on any of the requested ThreatList an empty response will be returned.
      public static void searchUri(String uri, [ThreatType](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.ThreatType.html) threatType) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `webRiskServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([WebRiskServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.cloud.webrisk.v1.WebRiskServiceClient.html) webRiskServiceClient = [WebRiskServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.cloud.webrisk.v1.WebRiskServiceClient.html).create()) {
    
          [SearchUrisRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.SearchUrisRequest.html) searchUrisRequest =
              [SearchUrisRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.SearchUrisRequest.html).newBuilder()
                  .addThreatTypes(threatType)
                  .setUri(uri)
                  .build();
    
          [SearchUrisResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.SearchUrisResponse.html) searchUrisResponse = webRiskServiceClient.searchUris(searchUrisRequest);
    
          if (!searchUrisResponse.[getThreat](https://docs.cloud.google.com/java/docs/reference/google-cloud-webrisk/latest/com.google.webrisk.v1.SearchUrisResponse.html#com_google_webrisk_v1_SearchUrisResponse_getThreat__)().getThreatTypesList().isEmpty()) {
            System.out.println("The URL has the following threat: ");
            System.out.println(searchUrisResponse);
          } else {
            System.out.println("The URL is safe!");
          }
        }
      }
    }

### Python

To authenticate to Web Risk, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest)
    from google.cloud.webrisk_v1 import [SearchUrisResponse](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.SearchUrisResponse.html)
    
    
    def search_uri(
        uri: str, threat_type: [webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest).[ThreatType](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.ThreatType.html).MALWARE
    ) -> SearchUrisResponse:
        """Checks whether a URI is on a given threatList.
    
        Multiple threatLists may be searched in a single query. The response will list all
        requested threatLists the URI was found to match. If the URI is not
        found on any of the requested ThreatList an empty response will be returned.
    
        Args:
            uri: The URI to be checked for matches
                Example: "http://testsafebrowsing.appspot.com/s/malware.html"
            threat_type: The ThreatLists to search in. Multiple ThreatLists may be specified.
                Example: threat_type = webrisk_v1.ThreatType.MALWARE
    
        Returns:
            SearchUrisResponse that contains a threat_type if the URI is present in the threatList.
        """
        webrisk_client = [webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest).[WebRiskServiceClient](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.services.web_risk_service.WebRiskServiceClient.html)()
    
        request = [webrisk_v1](https://docs.cloud.google.com/python/docs/reference/webrisk/latest).[SearchUrisRequest](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.SearchUrisRequest.html)()
        request.threat_types = [threat_type]
        request.uri = uri
    
        response = webrisk_client.[search_uris](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.services.web_risk_service.WebRiskServiceClient.html#google_cloud_webrisk_v1_services_web_risk_service_WebRiskServiceClient_search_uris)(request)
        if response.threat.threat_types:
            print(f"The URI has the following threat: {response}")
        else:
            print("The URL is safe!")
        return response
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=webrisk). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
