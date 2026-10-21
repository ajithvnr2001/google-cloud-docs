---
url: https://docs.cloud.google.com/apigee/docs/api-security/detection-rules/
title: Detection rules \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:56:34.830561+00:00
---

# Detection rules  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-security/detection-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Detection rules Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Advanced API Security uses _detection rules_ to detect unusual patterns in API traffic that could represent malicious activity. These rules include both machine learning models, trained on real API data, and descriptive rules, based on known types of API threats.

**Note:** The Advanced API Security [Abuse detection](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection) page uses detection rules to detect security incidents. A security incident is a group of events with similar patterns that could represent a security threat. Note that one incident might be triggered by multiple detection rules, in which case all of the rules that triggered the incident are listed in the Abuse detection [Environment details](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#environment-details) view.

The following table lists the detection rules and their descriptions.

Detection rule | Description  
---|---  
**Preview:** Advanced API Scraper | A machine learning model that detects API scraping, which is the process of extracting targeted information from APIs for malicious purposes.  
**Preview:** Advanced Anomaly Detection | A machine learning model for detecting anomalies—unusual patterns of events—in API traffic. See About Advanced Anomaly Detection.  
Brute Guessor | High proportion of response errors (4xx and 5xx) during previous 24 hours  
Flooder | High proportion of traffic from an IP address in a 5-minute window  
OAuth Abuser | Large number of OAuth sessions with small number of user agents during the previous 24 hours  
Robot Abuser | Large number of 403 rejection errors in the past 24 hours  
Static Content Scraper | High proportion of response payload size from an IP address in a 5-minute window  
TorListRule | Tor exit nodes IP list. A Tor exit node is the last Tor node that traffic passes through in the [Tor network](https://en.wikipedia.org/wiki/Tor_\(network\)) before exiting onto the internet. Detecting Tor exit nodes indicates that an agent has sent traffic to your APIs from the Tor network, possibly for malicious purposes.  
  
## About Advanced Anomaly Detection

The Advanced Anomaly Detection algorithm learns from your API traffic, taking into account factors like error rates, traffic volume, request size, latency, geolocation, and other traffic metadata at the environment level. If there are significant shifts in traffic patterns (for example, a surge in traffic, error rates, or latency), the model flags the IP address that contributed to the anomaly in Detected Traffic.

**Note:** Use of Advanced Anomaly Detection requires opting in to training the model on your API traffic data. For more information, see [ Opt in for machine learning models for Abuse Detection](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#opt-in-for-machine-learning-models-for-machine-learning).

You can also combine anomaly detection with [security actions](https://docs.cloud.google.com/apigee/docs/api-security/security-actions) to automatically flag or deny traffic that is detected as anomalous by the model. See the [ "Using Apigee Advanced API Security's Security Actions to Flag and Block Suspicious Traffic" community post](https://www.googlecloudcommunity.com/gc/Cloud-Product-Articles/Using-Apigee-Advanced-API-Security-s-Security-Actions-to-Flag/ta-p/842645) for additional information.

### Model behavior

To reduce the risk that bad actors can exploit the model, we do not expose specific details about how the model works or how incidents are detected. However, this additional information can help you make the best use of anomaly detection:

  * **Accounting for seasonal variance:** Because the model is trained on your traffic data, it can recognize and account for seasonal traffic variances (such as holiday traffic), if your traffic data includes previous data for that pattern, such as the same holiday in a previous year.
  * **Surfacing anomalies:**
    * **For existing Apigee and hybrid customers:** Apigee recommends that you have at least 2 weeks of historical API traffic data and, for more accurate results 12 weeks of historical data is preferable. Advanced Anomaly Detection starts surfacing anomalies within six hours of opting in to model training.
    * **New Apigee users:** The model starts surfacing anomalies 6 hours after opt-in, if you have a minimum of 2 weeks of historical data. However, we recommend using caution when acting on detected anomalies until the model has at least 12 weeks of data for training. The model is continuously trained on your historical traffic data so that it becomes more accurate over time.



### Limitations

For Abuse Detection Advanced Anomaly Detection, anomalies are detected at the environment level. Anomaly detection at an individual proxy level is not supported at this time.

## Machine learning and detection rules

Advanced API Security uses models built with Google's machine learning algorithms to detect security threats to your APIs. These models are pre-trained on real API traffic data sets (including your current traffic data, if enabled) that contain known security threats. As a result, the models learn to recognize unusual API traffic patterns, such as API scraping and anomalies, and cluster events together based on similar patterns. 

Two of the detection rules are based on machine learning models:

  * Advanced API Scraper
  * Advanced Anomaly Detection

**Note:** The data used to train the machine learning models for the rules Advanced API Scraper and Advanced Anomaly Detection contain metadata, including source IP address, source geography, and the values of some HTTP request headers. However, the detection data received by the models do not include the actual values of this metadata. The model makes detections based on the statistical properties of the data, not on the values of the metadata.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
