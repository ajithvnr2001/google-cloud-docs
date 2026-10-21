---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dialogflow/agent/query/
title: gcloud alpha dialogflow agent query \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:07:28.619638+00:00
---

# gcloud alpha dialogflow agent query  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dialogflow/agent/query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dialogflow agent query Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dialogflow agent query - send a text or audio conversational query to the agent of the current project 
SYNOPSIS
    

`gcloud alpha dialogflow agent query` (`--query-text`=`QUERY_TEXT` | `--audio-encoding`=`AUDIO_ENCODING` `--query-audio-file`=`QUERY_AUDIO_FILE` `--sample-rate`=`SAMPLE_RATE`) [`--language`=`LANGUAGE`; default="en"] [`--session`=`SESSION`; default=`"DEFAULT_SESSION"`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Send a text or audio conversational query to the agent of the current project. 
EXAMPLES
     To query the agent of the current project with text: 
    
    
    gcloud alpha dialogflow agent query --query-text="hi"

To query the agent of the current project with text in session `my-session`: 
    
    
    gcloud alpha dialogflow agent query --session="my-session" --query-text="hi"

To query the agent of the current project with audio: 
    
    
    gcloud alpha dialogflow agent query --query-audio-file="path/to/audio_file.wav" --sample-rate="16000" --audio-encoding="AUDIO_ENCODING_LINEAR_16"

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--query-text`=`QUERY_TEXT`
     Conversational query in the form of text. 
Or at least one of these can be specified: 

Audio file and config: 
`--audio-encoding`=`AUDIO_ENCODING`
     Encoding of the audio file. 

See here for more information: <https://cloud.google.com/dialogflow-enterprise/docs/reference/rest/v2/projects.agent.sessions/detectIntent#AudioEncoding>. 

`AUDIO_ENCODING` must be one of: `audio-encoding-alaw`, `audio-encoding-amr`, `audio-encoding-amr-wb`, `audio-encoding-flac`, `audio-encoding-linear-16`, `audio-encoding-mulaw`, `audio-encoding-ogg-opus`, `audio-encoding-speex-with-header-byte`, `audio-encoding-unspecified`. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--query-audio-file`=`QUERY_AUDIO_FILE`
     Path to an audio file to use as a conversational query. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--sample-rate`=`SAMPLE_RATE`
     Sample rate of the audio file in Hertz. 

This flag argument must be specified if any of the other arguments in this group are specified. 

OPTIONAL FLAGS
    

`--language`=`LANGUAGE`; default="en"
     The language code of the query. For information on supported languages, see: <https://dialogflow.com/docs/languages>. 
`--session`=`SESSION`; default=`"DEFAULT_SESSION"`
     ID of the session to send the query to. This can be any number or string up to 36 bytes. By default, a different random ID will be used for every request. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `dialogflow/v2` API. The full documentation for this API can be found at: <https://cloud.google.com/dialogflow/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
