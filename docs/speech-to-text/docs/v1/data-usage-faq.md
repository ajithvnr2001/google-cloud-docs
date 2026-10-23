---
url: https://docs.cloud.google.com/speech-to-text/docs/v1/data-usage-faq/
title: Data usage FAQ \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:25.339215+00:00
---

# Data usage FAQ  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/v1/data-usage-faq/

New Cloud Speech-to-Text users should use the [V2 API](https://docs.cloud.google.com/speech-to-text/docs). Read our [migration guide](https://docs.cloud.google.com/speech-to-text/docs/migration) to learn how to migrate existing projects to the latest version. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback 

#  Data usage FAQ Stay organized with collections  Save and categorize content based on your preferences. 

  * **Does Google use the text or audio I send to the Cloud Speech-to-Text API?**

If you are not enrolled in the [data logging opt-in program](https://docs.cloud.google.com/speech-to-text/docs/data-logging), Google does not use any of your content for any purpose except to provide you with the Cloud Speech-to-Text API service. Content includes, for example, audio sent to the API or any returned transcripts.

  * **Will Google share the audio I send to the Cloud Speech-to-Text API?**

Google does not make the audio content sent to the Cloud Speech-to-Text API available to anyone else except as necessary to provide the Cloud Speech-to-Text API service. For example, sometimes we might need to use a third-party vendor to help us provide some aspect of our services, such as data storage or transmission. In these cases, that vendor is under appropriate security and confidentiality contractual obligations. We don't share your audio with other parties for any other purpose.

  * **Will the audio I send to the Cloud Speech-to-Text API, the transcription results, or other information about the request itself, be stored on Google servers? If so, for how long and where is the information kept, and do I have access to it?**

When you send audio to the Cloud Speech-to-Text API streaming or sync endpoints, Google processes it in memory and does not store any customer data. Google temporarily logs some metadata about your Cloud Speech-to-Text API requests (such as the time the request was received and the size of the request) in order to improve our service and combat abuse.

When you send audio to the Cloud Speech-to-Text API async endpoint, the resulting transcript is stored for a period of approximately 5 days to give you time to retrieve the transcript. The input audio data is not stored by the Cloud Speech-to-Text API service. This is done strictly as a feature of the service, to enable convenient retrieval of the data. This data is not used by Google for any other purpose other than to deliver it to the user who requested that it be stored.

**Note:** Data from users that have opted-in to the [data logging opt-in program](https://docs.cloud.google.com/speech-to-text/docs/v1/data-logging) is governed by [those terms](https://docs.cloud.google.com/speech-to-text/docs/data-logging-terms).
  * **How does Google protect and ensure the security of the data I send to the Cloud Speech-to-Text API?**

For detailed information on Google Cloud security measures, see the [Google Cloud Platform Security page](https://cloud.google.com/security).

  * **Does Google use my data to improve Cloud Speech-to-Text API services?**

Google only uses data from customers who have opted in to [data logging](https://docs.cloud.google.com/speech-to-text/docs/v1/data-logging) and agreed to the relevant [terms](https://docs.cloud.google.com/speech-to-text/docs/data-logging-terms) to improve its services. Data from customers who have not opted in to data logging is not stored or used by Google for anything other than providing the service to the customer.

  * **Where is data sent to the Cloud Speech-to-Text API processed?**

Data sent to Cloud Speech-to-Text is processed globally. Users can define a specific endpoint in order to limit processing of their data to within the European Union or the United States (see the [multi-region endpoints](https://docs.cloud.google.com/speech-to-text/docs/v1/endpoints) documentation for details). Limiting processing to a single Google Cloud region is not supported.

  * **Does Google claim ownership of the content I send in the request to the Cloud Speech-to-Text API?**

Google does not claim any ownership in any of the content (including the audio data and returned transcript) that you transmit to the Cloud Speech-to-Text API.

  * **Can I resell the Cloud Speech-to-Text API?**

No, you are not permitted to resell the Cloud Speech-to-Text API service. You can still integrate Cloud Speech-to-Text API into applications of independent value.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
