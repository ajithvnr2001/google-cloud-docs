---
url: https://docs.cloud.google.com/livestream/docs/troubleshooting/
title: Troubleshoot \u00a0|\u00a0 Live Stream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:13.765936+00:00
---

# Troubleshoot  |  Live Stream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Guides ](https://docs.cloud.google.com/livestream/docs/overview)



Send feedback 

#  Troubleshoot Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with the Live Stream API. The errors shown on this page are specific to the Live Stream API. For information on generic errors across Google APIs, see the Cloud APIs [Errors](https://docs.cloud.google.com/apis/design/errors) page.

## Input stream rejected

If your encoder sends an input stream to an input endpoint, but the connection keeps getting rejected, check for these possible issues:

### Invalid input endpoint URI

An error occurs if your encoder sends an input stream to an invalid input endpoint URI.

To resolve this issue, check if your encoder is configured to send the input stream to an input endpoint URI with the [correct IP address and `STREAM-ID`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#Input.FIELDS.uri).

### Input is not attached to a channel

An error occurs if your encoder sends an input stream to an input endpoint URI that is not attached to a channel.

To resolve this issue, [create a new channel](https://docs.cloud.google.com/livestream/docs/how-to/create-channels#create_channel) with the input endpoint. To check if an input endpoint has been successfully attached to the channel, [get the channel details](https://docs.cloud.google.com/livestream/docs/how-to/create-channels#get_channel_details) and look for the name of the input endpoint in the `inputAttachments` field.

### Inactive channel

An error occurs if your encoder sends an input stream to a channel that is not running.

To resolve this issue, [check the status](https://docs.cloud.google.com/livestream/docs/how-to/create-channels#get_channel_details) of the channel to make sure its `streamingState` is `AWAITING_INPUT`. If the `streamingState` of the channel is `STOPPED`, [start the channel](https://docs.cloud.google.com/livestream/docs/how-to/create-channels#start_channel).

### Another encoder already connected with the same input endpoint

An error occurs if multiple encoders attempt to send input streams to the same input endpoint. Only one connection is accepted at a time per input endpoint URI.

To resolve this issue, [check if the channel](https://docs.cloud.google.com/livestream/docs/how-to/create-channels#get_channel_details) is already in `STREAMING` state. If so, you have the following options:

  * Create a separate input endpoint and channel for the second input stream.

  * Stop the first input stream before sending another one to the same input endpoint.




### Encoder IP address is not in the allowed IP ranges

An error occurs if your encoder sends an input stream from an IP address outside the specified IP ranges configured for an input endpoint.

To resolve this issue, [get the details](https://docs.cloud.google.com/livestream/docs/how-to/create-input-endpoints#get_input_endpoint_details) for an input endpoint and check the [`securityRules`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#securityrule) field. If there are specified `ipRanges`, make sure your encoder has a valid IP address in those IP ranges.

## Missing output files in the Cloud Storage bucket

If your encoder is successfully sending an input stream to the input endpoint, but no output files appear in the Cloud Storage bucket, check for these possible issues:

### Incorrect Cloud Storage bucket

Output files may be missing if you are checking the wrong Cloud Storage bucket.

To resolve this issue, [get the channel details](https://docs.cloud.google.com/livestream/docs/how-to/create-channels#get_channel_details) for your live stream. Check the `output.uri` field for the correct Cloud Storage bucket URI.

### Invalid input video/audio codecs

Output files may be missing if your encoder is sending invalid video or audio codecs.

To resolve this issue, make sure your encoder is only sending H264 video and AAC audio codecs.

### Cloud Storage permission denied

By default, the Live Stream API creates a service account that can access Cloud Storage buckets in the same Google Cloud project that hosts the Live Stream API resources. Output files may be missing if this service account loses permission to access the Cloud Storage bucket.

To resolve this issue, make sure the service account has sufficient permissions. The creation of output files may fail for the following reasons:

  * The output Cloud Storage bucket is in a different Google Cloud project from Live Stream API resources such as the channel and input endpoint.

  * The default permissions are revoked from the service account.




See [Access to Cloud Storage](https://docs.cloud.google.com/livestream/docs/access-control#access_to_gcs) for more information.

### Missing audio tracks

Output files may be missing if your encoder sends an input stream with missing audio tracks. The video pipeline waits for all audio tracks to arrive before processing begins.

To resolve this issue, [get the channel details](https://docs.cloud.google.com/livestream/docs/how-to/create-channels#get_channel_details) for your live stream. Make sure your encoder is sending all audio tracks configured in the `ElementaryStream.audioStream.mapping` ([`AudioMapping`](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#audiomapping)) field.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
