---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/examples-custom-infotypes/
title: Examples of custom infotype detectors \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:31.074395+00:00
---

# Examples of custom infotype detectors  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/examples-custom-infotypes/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Examples of custom infotype detectors Stay organized with collections  Save and categorize content based on your preferences. 

### Protocol

The sample JSON objects on this page are a few examples of Sensitive Data Protection [custom infoType detectors](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes) that you can use during inspection and de-identification.

For more information about the different kinds of custom infoType detectors and how to create them, see [Creating custom infoType detectors](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes).

## Example `customInfoTypes` contents

The JSON given in the following table can be inserted into any [inspection](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers) or [de-identification](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data) job definition, inside the [`"customInfoTypes"`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#CustomInfoType) attribute. The following complete JSON request, which sends a short string to Sensitive Data Protection, includes a custom infoType detector definition that defines a medical record number format.

**JSON input:**
    
    
    POST https://dlp.googleapis.com/v2/projects/[PROJECT_ID]/content:inspect?key={YOUR_API_KEY}
    
    {
      "item":{
        "value":"Patients MRN 444-5-22222"
      },
      "inspectConfig":{
        "customInfoTypes":[
          {
            "infoType":{
              "name":"C_MRN"
            },
            "regex":{
              "pattern":"[1-9]{3}-[1-9]{1}-[1-9]{5}"
            },
            "likelihood":"POSSIBLE"
          }
        ]
      }
    }
    

Example description | Custom infoType detector  
---|---  
Generic alpha-numeric identifier  | 
    
    
    {
      "infoType":{
        "name":"GENERIC_ID2"
      },
      "regex":{
        "pattern":"\\b(([0-9]|([a-zA-Z()]{1,2}[0-9]{1}))[0-9-\\[\\]:(), ._]+)[0-9]{1}"
      },
      "likelihood":"POSSIBLE"
    }  
  
Generic currency  | 
    
    
    {
      "infoType":{
        "name":"GENERIC_CURRENCY"
      },
      "regex":{
        "pattern":"((\\p{Sc}{1})( ){0,1}[0-9,()]+)(.){0,1}[0-9]{0,}"
      },
      "likelihood":"VERY_LIKELY"
    }  
  
Generic percentage  | 
    
    
    {
      "infoType":{
        "name":"GENERIC_PERCENT"
      },
      "regex":{
        "pattern":"\\b([0-9,.()]+)( ){0,1}(%){1}"
      },
      "likelihood":"VERY_LIKELY"
    }  
  
Generic unit of measurement  | 
    
    
    {
      "infoType":{
        "name":"GENERIC_MEASURE"
      },
      "regex":{
        "pattern":"(?i)([0-9])([0-9,.]+)( ){0,1}(?i)(°C|°F|K|°Ré|°N|°Ra|m³|dm³|cm³|l|dl|cl|ml|fl oz|in³|ft³|yd³|gal|bbl|pt|km|m|dm|cm|mm|mi|in|ft|yd|nautical mile|kg|hg|g|dg|cg|mg|µg|mcg|carat|grain|oz|lb|cwt|ton|km²|m²|dm²|cm²|mm²|ha|ca|mile²|in²|yd²|ft²|acre|nautical mile²|kmph|mps|mph|knot|km/h|m/s|mi/h|Hz|KHz|MHz|GHz|atm|bar|mbar|Pa|hPa|Psi|Torr|J|KJ|cal|kcal|Wh|kWh|BTU|thm|ft-lb|degrees|Celsius|Fahrenheit|Kelvin|Reaumur|Newton|Rankine|cubic |liter|deciliter|centiliter|milliliter|fluid ounce|gallon|petroleum barrel|pint|kilometer|meter|decimeter|centimeter|millimeter|mile|inch|foot|yard|nautical mile|tonne|kilogram|hectogram|gram|decigram|centigram|milligram|microgram|carat|grain|ounce|pound|square|hectare|centiare|square mile|square inch|square yard|square foot|acre|square nautical mile|kilometer|meter|mile per hour|knot|Hertz|Kilohertz|Megahertz|Gigahertz|Atmosphère|Bar|Millibar|Pascal|Hectopascal|Torr|Joule|Kilojoule|Calorie|Kilocalorie|Watt-hour|Kilowatt-hour|Foot-Pound|mpg){1}(s){0,1}\\b"
      },
      "likelihood":"VERY_LIKELY"
    }  
  
Generic Requests for Comments (RFC) identifier  | 
    
    
    {
      "infoType":{
        "name":"GENERIC_RFC"
      },
      "regex":{
        "pattern":"\\b(?i)(rfc)( ){0,1}(20|768|783|791|792|793|826|854|855|862|863|864|868|903|937|951|959|1034|1035|1036|1055|1058|1059|1087|1119|1149|1157|1176|1305|1321|1350|1436|1441|1459|1730|1777|1855|1918|1939|1945|1948|1950|1951|1952|1964|2080|2119|2131|2177|2195|2228|2230|2246|2251|2252|2253|2254|2255|2256|2326|2327|2328|2351|2362|2397|2407|2408|2409|2427|2453|2460|2549|2555|2570|2595|2606|2740|2743|2744|2810|2811|2812|2813|2853|2865|2866|2974|3022|3031|3053|3056|3080|3162|3207|3261|3284|3286|3315|3339|3376|3401|3402|3403|3404|3405|3492|3501|3530|3550|3711|3720|3730|3783|3801|3830|3977|4122|4213|4217|4271|4287|4251|4291|4353|4408|4422|4541|4575|4579|4634|4646|4655|4787|4880|4960|5023|5321|5322|5533|5545|5849|5880|5881|5905|5969|6238|6265|6409|6455|6508|6726|6749|6797|6805|7230|7231|7232|7233|7234|7235|7301|7348|7469|7540|7541|7567|7725|7871|8391){0,1}"
      },
      "likelihood":"LIKELY"
    }  
  
Generic RJ45 network connector identifier  | 
    
    
    {
      "infoType":{
        "name":"GENERIC_RJ_NETWORK"
      },
      "regex":{
        "pattern":"\\b(?i)(rj)(-){0,1}(?i)(A1X|A2X|A3X|2MB|11|12|13|14|15C|18|21X|25|26X|27X|31X|32X|33X|34X|35X|38X|41S|45S|45|48C|48S|48X|49C|61X|71C)"
      },
      "likelihood":"VERY_LIKELY"
    }  
  
Generic data size  | 
    
    
    {
      "infoType":{
        "name":"GENERIC_DATA_SIZE"
      },
      "regex":{
        "pattern":"\\b([0-9,. ]+)(?i)(byte|Kilobyte|KiB|Kilobit|kbit|bit|Megabyte|MiB|Megabit|Mbit|meg|Gigabyte|GiB|Gigabit|Gbit|gig|Terabyte|TiB|Terabit|Tbit|Petabyte|PiB|Petabit|Pbit|Exabyte|EiB|Exabit|Ebit|Zettabyte|ZiB|Zettabit|Zbit|Yottabyte|YiB|Yottabit|Ybit|KB|MB|GB|TB|PB|EB|ZB|YB)(p){0,1}(s){0,1}"
      },
      "likelihood":"VERY_LIKELY"
    }  
  
Numerical identifier  | 
    
    
    {
      "infoType":{
        "name":"GENERIC_ID1"
      },
      "regex":{
        "pattern":"\\w*[0-9][0-9-()\\[\\].:/]+[0-9]\\w*"
      },
      "likelihood":"POSSIBLE"
    }  
  
### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html);
    import com.google.privacy.dlp.v2.[ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html).[BytesType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.BytesType.html);
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[Regex](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.html);
    import com.google.privacy.dlp.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Finding.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html);
    import com.google.privacy.dlp.v2.[InspectContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html);
    import com.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    
    public class InspectWithCustomRegex {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String textToInspect = "Patients MRN 444-5-22222";
        String customRegexPattern = "[1-9]{3}-[1-9]{1}-[1-9]{5}";
        inspectWithCustomRegex(projectId, textToInspect, customRegexPattern);
      }
    
      // Inspects a BigQuery Table
      public static void inspectWithCustomRegex(
          String projectId, String textToInspect, String customRegexPattern) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the type and content to be inspected.
          [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html) byteItem =
              [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html).newBuilder()
                  .setType([BytesType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.BytesType.html).TEXT_UTF8)
                  .[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.Builder.html#com_google_privacy_dlp_v2_ByteContentItem_Builder_setData_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(textToInspect))
                  .build();
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) item = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setByteItem(byteItem).build();
    
          // Specify the regex pattern the inspection will look for.
          [Regex](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.html) regex = [Regex](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.html).newBuilder().[setPattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Regex_Builder_setPattern_java_lang_String_)(customRegexPattern).build();
    
          // Construct the custom regex detector.
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) infoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("C_MRN").build();
          [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html) customInfoType =
              [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).newBuilder().setInfoType(infoType).setRegex(regex).build();
    
          // Construct the configuration for the Inspect request.
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) config =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .[addCustomInfoTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addCustomInfoTypes_com_google_privacy_dlp_v2_CustomInfoType_)(customInfoType)
                  .[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true)
                  .setMinLikelihood([Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html).POSSIBLE)
                  .build();
    
          // Construct the Inspect request to be sent by the client.
          [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html) request =
              [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(item)
                  .setInspectConfig(config)
                  .build();
    
          // Use the client to send the API request.
          [InspectContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html) response = dlp.inspectContent(request);
    
          // Parse the response and process results
          System.out.println("Findings: " + response.[getResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html#com_google_privacy_dlp_v2_InspectContentResponse_getResult__)().getFindingsCount());
          for ([Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Finding.html) f : response.[getResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html#com_google_privacy_dlp_v2_InspectContentResponse_getResult__)().getFindingsList()) {
            System.out.println("\tQuote: " + f.getQuote());
            System.out.println("\tInfo type: " + f.getInfoType().getName());
            System.out.println("\tLikelihood: " + f.getLikelihood());
          }
        }
      }
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
