---
url: https://docs.cloud.google.com/speech-to-text/docs/v1/measure-accuracy/
title: Measure and improve accuracy \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:03.931270+00:00
---

# Measure and improve accuracy  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/v1/measure-accuracy/

New Cloud Speech-to-Text users should use the [V2 API](https://docs.cloud.google.com/speech-to-text/docs). Read our [migration guide](https://docs.cloud.google.com/speech-to-text/docs/migration) to learn how to migrate existing projects to the latest version. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback 

#  Measure and improve accuracy Stay organized with collections  Save and categorize content based on your preferences. 

In this quickstart, learn how to measure and improve the accuracy of the Google Cloud Cloud Speech-to-Text for your audio data. Also explore the various models and options available from the API to enhance transcription accuracy. Explore how to use the Cloud Speech-to-Text UI in the Google Cloud console and a ground-truth file to measure accuracy and to gain insights into the Cloud Speech-to-Text system.

Machine Learning (ML) systems are inherently subject to inaccuracies, and Automatic Speech Recognition (ASR) systems, also known as Cloud Speech-to-Text systems, are no exception. Accurate measurement of accuracy is strongly coupled to specific use cases and the systems being evaluated, as differences in audio recording quality and acoustic conditions can significantly impact accuracy. As a result, a singular accuracy score for all customers and use cases is impractical. To ensure reliable performance of ASR systems in critical production-facing systems performance. It is also essential to understand how Cloud Speech-to-Text performs within the broader context of your system.

For the purposes of this quickstart guide,use the industry standard method for comparison, [Word Error Rate (WER)](https://en.wikipedia.org/wiki/Word_error_rate), often abbreviated as WER. For more information on how WER is calculated and interpreted see [Measure and improve speech accuracy](https://docs.cloud.google.com/speech-to-text/docs/v1/speech-accuracy).

## Get started with the Google Cloud console

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `storage.buckets.get`
  * `storage.buckets.list`



At the project or bucket level:

  * `storage.objects.create`
  * `storage.objects.get`
  * `storage.objects.list`
  * `storage.objects.update`



Ensure you have signed up for a Google Cloud account and created a project.

  1. Go to **Speech** in the Google Cloud console, and navigate to the [Cloud Speech-to-Text UI](https://console.cloud.google.com/speech).
  2. Using an audio file that is acoustically representative of your use case and how you are planning to use the ASR system, follow the quickstart instructions for making your first transcription using the [Cloud Speech-to-Text](https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-console).



## Calculating transcription accuracy

  1. After you have successfully transcribed your audio file, use the **Transcription accuracy** section. This section remains empty until accuracy is calculated for your transcription.
  2. Using the **Upload ground truth** button at the top of the section, you can begin calculating accuracy.

![Cloud Speech-to-Text transcription details page, highlighting the transcription accuracy section and the upload ground truth button.](https://docs.cloud.google.com/static/speech-to-text/docs/images/stt_transcription_details.png)Cloud Speech-to-Text transcription details page, highlighting the transcription accuracy section and the upload ground truth button.

## Specifying ground truth

  1. To calculate the accuracy of the transcription, provide a ground truth file. This is a TXT or CSV file, usually a human-generated transcription file that contains the correct or expected transcriptions for comparison.
  2. Using `gs://cloud-samples-data/speech/brooklyn_bridge.wav` as an example. The ground truth file contains: `How old is the Brooklyn Bridge`. If you don't have a ground truth file available, a recommendation is to download the transcription in a text format. Edit the transcription file as needed. Upload the transcription file as the ground truth file.
  3. Using **Upload** or an existing Cloud Storage file, specify the ground truth file, and click **Save**.

![Cloud Speech-to-Text transcription creation page, showing options to select or upload a ground truth file.](https://docs.cloud.google.com/static/speech-to-text/docs/images/stt_upload_ground_truth.png)Cloud Speech-to-Text transcription creation page, showing options to select or upload a ground truth file.

## Confirming ground truth

  1. After clicking **Save** , a prompt displays to confirm that the specified ground truth file is correct. Verify that the ground truth file accurately represents the correct transcriptions, as it directly affects the accuracy metrics.
  2. Click **Confirm** to proceed.

![Cloud Speech-to-Text transcription page, showing the contents of the uploaded ground truth file.](https://docs.cloud.google.com/static/speech-to-text/docs/images/stt_ground_truth_confirmation.png)Cloud Speech-to-Text transcription page, showing the contents of the uploaded ground truth file.

## Review evaluation results

  1. Depending on the size of the input data, the evaluation process might take some time, and the results are displayed upon completion.
  2. Once the evaluation is complete, the following sections are displayed: 
     * The **Transcription accuracy** table, the accuracy metrics, and a link to the ground truth file that were used in the process.
     * The `Transcription` with a toggle for comparing to the ground truth file along with a breakdown of accuracy metrics and highlights.
  3. Review and interpret the accuracy results to understand the performance of the Cloud Speech-to-Text recognizer that are used to identify areas for improvement, as the results vary depending on the inputs and transcription used. In the following examples, you can see indicative cases of the accuracy results, which provide valuable insights for optimization of the Cloud Speech-to-Text system. 
     * An example of 0% WER: ![Cloud Speech-to-Text transcription accuracy page, showing computed evaluation results for the given transcript with 0% word error rate.](https://docs.cloud.google.com/static/speech-to-text/docs/images/stt_accuracy_0_wer.png)Cloud Speech-to-Text transcription accuracy page, showing computed evaluation results for the given transcript with 0% word error rate.
     * An example of 40% WER: ![Cloud Speech-to-Text transcription accuracy page, showing computed evaluation results for the given transcript with 40% word error rate.](https://docs.cloud.google.com/static/speech-to-text/docs/images/stt_accuracy_40_wer.png)Cloud Speech-to-Text transcription accuracy page, showing computed evaluation results for the given transcript with 40% word error rate.



## Optional: Updating ground truth

You can test a different ground truth against the existing transcription, by reattaching a different file and then repeating steps three and four with an updated ground truth file.

##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud STT performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud STT free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
