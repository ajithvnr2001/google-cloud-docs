---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fingerprint-js/
title: Collect Fingerprint logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:19:52.814506+00:00
---

# Collect Fingerprint logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fingerprint-js/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Fingerprint logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to configure Fingerprint (formerly FingerprintJS) to push logs to Google Security Operations using webhooks.

Fingerprint is a device intelligence platform that provides visitor identification and fraud detection capabilities. It generates unique visitor identifiers and provides smart signals including bot detection, VPN detection, incognito mode detection, and other device intelligence insights. When a visitor is identified through the FingerprintJS JavaScript agent, webhooks can send the identification event data to Google Security Operations in real time.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * FingerprintJS account with webhook support
  * Access to Google Cloud Console (for API key creation)
  * FingerprintJS JavaScript agent installed on your website or application



## Create webhook feed in Google SecOps

### Create the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `FingerprintJS Identification Events`).
  5. Select **Webhook** as the **Source type**.
  6. Select **FingerprintJS** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** (optional): Leave empty. Each webhook request contains a single identification event.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  9. Click **Next**.
  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



### Generate and save secret key

After creating the feed, you must generate a secret key for authentication:

  1. On the feed details page, click **Generate Secret Key**.
  2. A dialog displays the secret key.
  3. Copy and save the secret key securely.



**Important** : The secret key is displayed only once and cannot be retrieved later. If you lose it, you must generate a new secret key.

### Get the feed endpoint URL

  1. Go to the **Details** tab of the feed.
  2. In the **Endpoint Information** section, copy the **Feed endpoint URL**.
  3. The URL format is:
         
         https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate
         

or
         
         https://<REGION>-malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate
         

  4. Save this URL for the next steps.

  5. Click **Done**.




## Create Google Cloud API key

Chronicle requires an API key for authentication. Create a restricted API key in the Google Cloud Console.

### Create the API key

  1. Go to the [Google Cloud Console Credentials page](https://console.cloud.google.com/apis/credentials).
  2. Select your project (the project associated with your Chronicle instance).
  3. Click **Create credentials > API key**.
  4. An API key is created and displayed in a dialog.
  5. Click **Edit API key** to restrict the key.



### Restrict the API key

  1. In the **API key** settings page: 
     * **Name** : Enter a descriptive name (for example, `Chronicle FingerprintJS Webhook API Key`).
  2. Under **API restrictions** : 
     1. Select **Restrict key**.
     2. In the **Select APIs** dropdown, search for and select **Google SecOps API** (or **Chronicle API**).
  3. Click **Save**.
  4. Copy the API key value from the **API key** field at the top of the page.
  5. Save the API key securely.

**Note:** Restricting the API key ensures it can only be used with the Chronicle API, reducing security risk if the key is compromised.



## Configure FingerprintJS webhook

### Construct the webhook URL

  * Combine the Chronicle endpoint URL and API key:
        
        <ENDPOINT_URL>?key=<API_KEY>
        

    * **Example:**
          
          https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=AIzaSyD...
          




### Create webhook in FingerprintJS Dashboard

  1. Sign in to the **FingerprintJS Dashboard**.
  2. Go to **Dashboard > Webhooks**.
  3. Click **Add webhook**.
  4. Provide the following configuration details: 
     * **URL** : Paste the complete endpoint URL with API key from above.
     * **Environment** (optional): If you select an environment, your webhook will only report on events from a matching environment. Leave empty to receive events from all environments.
     * **Basic authentication** (optional): Expand **Basic authentication** if you want to add additional authentication. For Chronicle integration, you can leave this empty as authentication is handled via the API key and secret key.
  5. Click **Create Webhook**.
  6. A success modal displays **Webhooks created**.
  7. **Important** : If you are using webhook signatures (Enterprise plan only), copy and save the encryption key shown in the success modal. The key is displayed only once.



### Add Chronicle secret key to webhook

FingerprintJS does not support custom HTTP headers during webhook creation. You must add the Chronicle secret key as a query parameter in the webhook URL.

  * Update the webhook URL to include the secret key:
        
        <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>
        

    * **Example:**
          
          https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=AIzaSyD...&secret=abcd1234...
          




To update the webhook URL:

  1. In the FingerprintJS Dashboard, go to **Dashboard > Webhooks**.
  2. Find your webhook in the table and click the **Edit** icon.
  3. Update the **URL** field with the complete URL including both API key and secret key.
  4. Click **Edit webhook**.



### Test the webhook

  1. In the FingerprintJS Dashboard, go to **Dashboard > Webhooks**.
  2. Find your webhook in the table.
  3. Click **Send test event**.
  4. Wait for confirmation that the test event was sent successfully.
  5. Verify the webhook shows a successful delivery status.

**Note:** FingerprintJS expects your endpoint to respond with a 2xx status code within 3 seconds. If the endpoint does not respond within this timeframe, the webhook will be marked as failed and retried once after 5 minutes.



## Authentication methods reference

Chronicle webhook feeds support multiple authentication methods. FingerprintJS webhooks use query parameters for authentication.

### Query parameters method

FingerprintJS does not support custom HTTP headers during webhook creation, so credentials must be appended to the URL.

  * **URL format:**
        
        <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>
        

    * **Example:**
          
          https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=AIzaSyD...&secret=abcd1234...
          

  * **Request format:**
        
        POST <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY> HTTP/1.1
        Content-Type: application/json
        
        {
          "visitorId": "3HNey93AkBW6CRbxV6xP",
          "requestId": "1708102555327.NLOjmg",
          "timestamp": 1582299576512
        }
        


**Note:** Credentials are visible in the URL and may be logged in web server access logs. This is the only authentication method supported by FingerprintJS webhooks.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
rawDeviceAttributes.architecture.value, rawDeviceAttributes.audio.value, rawDeviceAttributes.colorDepth.value, rawDeviceAttributes.colorGamut.value, rawDeviceAttributes.contrast.value, rawDeviceAttributes.cookiesEnabled.value, rawDeviceAttributes.deviceMemory.value, rawDeviceAttributes.fonts.value, rawDeviceAttributes.forcedColors.value, rawDeviceAttributes.hardwareConcurrency.value, rawDeviceAttributes.hdr.value, rawDeviceAttributes.indexedDB.value, rawDeviceAttributes.localStorage.value, rawDeviceAttributes.math.value, rawDeviceAttributes.monochrome.value, rawDeviceAttributes.openDatabase.value, rawDeviceAttributes.pdfViewerEnabled.value, rawDeviceAttributes.reducedMotion.value, rawDeviceAttributes.screenFrame.value, rawDeviceAttributes.screenResolution.value, rawDeviceAttributes.sessionStorage.value, rawDeviceAttributes.touchSupport.value.maxTouchPoints, rawDeviceAttributes.languages.value, rawDeviceAttributes.vendorFlavors.value, rawDeviceAttributes.fontPreferences.value.apple, rawDeviceAttributes.fontPreferences.value.default, rawDeviceAttributes.fontPreferences.value.min, rawDeviceAttributes.fontPreferences.value.mono, rawDeviceAttributes.fontPreferences.value.sans, rawDeviceAttributes.fontPreferences.value.serif, rawDeviceAttributes.fontPreferences.value.system | additional.fields | Merged from labels created from source fields  
has_principal, has_target, has_target_resource | metadata.event_type | Set to "NETWORK_CONNECTION" if has_principal and has_target true, else "USER_RESOURCE_ACCESS" if has_target_resource true, else "STATUS_UPDATE" if has_principal true, else "GENERIC_EVENT"  
source_type | metadata.product_event_type | Value copied directly  
requestId | metadata.product_log_id | Value copied directly  
browserDetails.userAgent | network.http.parsed_user_agent | Parsed from browserDetails.userAgent  
browserDetails.browserName | network.http.parsed_user_agent.browser | Value copied directly  
browserDetails.browserFullVersion | network.http.parsed_user_agent.browser_version | Value copied directly  
browserDetails.device | network.http.parsed_user_agent.device | Value copied directly  
| network.http.parsed_user_agent.family | Set to "USER_DEFINED"  
browserDetails.os | network.http.parsed_user_agent.os | Value copied directly  
browserDetails.clientReferrer | network.http.referral_url | Value copied directly  
browserDetails.userAgent, userAgent | network.http.user_agent | Value from userAgent if not empty, else browserDetails.userAgent  
tag.session | network.session_id | Value copied directly  
rawDeviceAttributes.vendor.value | principal.administrative_domain | Value copied directly  
ip | principal.asset.ip | Value copied directly  
ip | principal.ip | Value copied directly  
ipInfo.v4.geolocation.city.name | principal.location.city | Value copied directly  
ipInfo.v4.geolocation.country.name | principal.location.country_or_region | Value copied directly  
ipInfo.v4.geolocation.latitude | principal.location.region_coordinates.latitude | Converted to float  
ipInfo.v4.geolocation.longitude | principal.location.region_coordinates.longitude | Converted to float  
browserDetails.osVersion, rawDeviceAttributes.platform.value | principal.platform_version | Value from rawDeviceAttributes.platform.value if not empty, else browserDetails.osVersion  
ipInfo.v4.asn.asn, ipInfo.v4.asn.network, ipInfo.v4.asn.name, ipInfo.v4.geolocation.accuracyRadius, ipInfo.v4.geolocation.continent.name, ipInfo.v4.geolocation.timezone, ipInfo.v4.geolocation.subdivisions.isoCode, ipInfo.v4.geolocation.subdivisions.name | principal.resource.attribute.labels | Merged from labels created from source fields  
bot.result, browserDetails.browserMajorVersion, confidence.score, confidence.revision, developerTools.result, highActivity.result, incognito, ipBlocklist.result, ipBlocklist.details.attackSource, ipBlocklist.details.emailSpam, visitorFound, visitorId, tag.request, privacySettings.result, proxy.result, suspectScore.result, tor.result, virtualMachine.result, tampering.anomalyScore, tampering.antiDetectBrowser, tampering.result, vpn.confidence, vpn.originCountry, vpn.originTimezone, vpn.result, vpn.methods.auxiliaryMobile, vpn.methods.osMismatch, vpn.methods.publicVPN, vpn.methods.timezoneMismatch, velocity.distinctCountry.intervals.1h, velocity.distinctCountry.intervals.24h, velocity.distinctCountry.intervals.5m, velocity.distinctIp.intervals.1h, velocity.distinctIp.intervals.24h, velocity.distinctIp.intervals.5m, velocity.events.intervals.1h, velocity.events.intervals.24h, velocity.events.intervals.5m, velocity.ipEvents.intervals.1h, velocity.ipEvents.intervals.24h, velocity.ipEvents.intervals.5m, rawDeviceAttributes.webGlBasics.value.renderer, rawDeviceAttributes.webGlBasics.value.rendererUnmasked, rawDeviceAttributes.webGlBasics.value.vendorUnmasked, rawDeviceAttributes.webGlBasics.value.shadingLanguageVersion, rawDeviceAttributes.webGlExtensions.value.contextAttributes, rawDeviceAttributes.webGlExtensions.value.extensions, rawDeviceAttributes.webGlExtensions.value.extensionParameters, rawDeviceAttributes.webGlExtensions.value.parameters, rawDeviceAttributes.webGlExtensions.value.shaderPrecisions, rawDeviceAttributes.mathML.value.bottom, rawDeviceAttributes.mathML.value.top, rawDeviceAttributes.mathML.value.left, rawDeviceAttributes.mathML.value.right, rawDeviceAttributes.mathML.value.width, rawDeviceAttributes.mathML.value.height, rawDeviceAttributes.mathML.value.font, rawDeviceAttributes.mathML.value.x, rawDeviceAttributes.mathML.value.y, rawDeviceAttributes.emoji.value.bottom, rawDeviceAttributes.emoji.value.top, rawDeviceAttributes.emoji.value.left, rawDeviceAttributes.emoji.value.right, rawDeviceAttributes.emoji.value.width, rawDeviceAttributes.emoji.value.height, rawDeviceAttributes.emoji.value.font, rawDeviceAttributes.emoji.value.x, rawDeviceAttributes.emoji.value.y, rawDeviceAttributes.canvas.value.Geometry, rawDeviceAttributes.canvas.value.Text, rawDeviceAttributes.canvas.value.Winding | security_result.detection_fields | Merged from labels created from source fields  
rawDeviceAttributes.webGlBasics.value.vendor | target.administrative_domain | Value copied directly  
ipInfo.v6.address | target.asset.ip | Value copied directly  
ipInfo.v6.address | target.ip | Value copied directly  
ipInfo.v6.geolocation.city.name | target.location.city | Value copied directly  
ipInfo.v6.geolocation.country.name | target.location.country_or_region | Value copied directly  
ipInfo.v6.geolocation.latitude | target.location.region_coordinates.latitude | Converted to float  
ipInfo.v6.geolocation.longitude | target.location.region_coordinates.longitude | Converted to float  
path | target.path | Value copied directly  
rawDeviceAttributes.webGlBasics.value.version | target.platform_version | Value copied directly  
ipInfo.v6.asn.asn, ipInfo.v6.asn.network, ipInfo.v6.asn.name, ipInfo.v6.geolocation.accuracyRadius, ipInfo.v6.geolocation.continent.name, ipInfo.v6.geolocation.timezone, ipInfo.v6.geolocation.subdivisions.isoCode, ipInfo.v6.geolocation.subdivisions.name | target.resource.attribute.labels | Merged from labels created from source fields  
url | target.url | Value copied directly  
| metadata.product_name | Set to "FINGERPRINT_JS"  
| metadata.vendor_name | Set to "FINGERPRINT_JS"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fingerprint-js-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
