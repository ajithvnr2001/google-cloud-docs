---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-translate-v2/latest/Google-Cloud-Translate-V2-Api/
title: Cloud Translation V2 API - Class Google::Cloud::Translate::V2::Api (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:40:06.715098+00:00
---

# Cloud Translation V2 API - Class Google::Cloud::Translate::V2::Api (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-translate-v2/latest/Google-Cloud-Translate-V2-Api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Translation V2 API - Class Google::Cloud::Translate::V2::Api (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.1  0.5.1  0.4.1  0.3.1 

Reference documentation and code samples for the Cloud Translation V2 API class Google::Cloud::Translate::V2::Api.

## Api

Represents top-level access to the Google Cloud Translation API. Translation API supports more than one hundred different languages, from Afrikaans to Zulu. Used in combination, this enables translation between thousands of language pairs. Also, you can send in HTML and receive HTML with translated text back. You don't need to extract your source text or reassemble the translated content.

## Inherits

  * Object 



## Example
    
    
    require "google/cloud/translate/v2"
    
    translate = Google::Cloud::Translate::V2.new
    
    translation = translate.translate "Hello world!", to: "la"
    
    translation.to_s #=> "Salve mundi!"
    
    translation.from #=> "en"
    translation.origin #=> "Hello world!"
    translation.to #=> "la"
    translation.text #=> "Salve mundi!"

## Methods 

### #detect
    
    
    def detect(*text) -> Detection, Array<Detection>

Detect the most likely language or languages of a text or multiple texts.

**Parameter**

  * **text** (String) — The text or texts upon which language detection should be performed. 



**Returns**

  * ([Detection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-translate-v2/latest/Google-Cloud-Translate-V2-Detection), Array<[Detection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-translate-v2/latest/Google-Cloud-Translate-V2-Detection)>) — A single [Detection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-translate-v2/latest/Google-Cloud-Translate-V2-Detection "Google::Cloud::Translate::V2::Detection \(class\)") object if just one text was given, or an array of [Detection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-translate-v2/latest/Google-Cloud-Translate-V2-Detection "Google::Cloud::Translate::V2::Detection \(class\)") objects if multiple texts were given. 



**Examples**
    
    
    require "google/cloud/translate/v2"
    
    translate = Google::Cloud::Translate::V2.new
    
    detection = translate.detect "Hello world!"
    detection.language #=> "en"
    detection.confidence #=> 0.7100697

Detecting multiple texts.
    
    
    require "google/cloud/translate/v2"
    
    translate = Google::Cloud::Translate::V2.new
    
    detections = translate.detect "Hello world!",
                                  "Bonjour le monde!"
    detections.count #=> 2
    detections.first.language #=> "en"
    detections.first.confidence #=> 0.7100697
    detections.last.language #=> "fr"
    detections.last.confidence #=> 0.40440267

### #languages
    
    
    def languages(language = nil) -> Array<Language>

List the languages supported by the API. These are the languages to and from which text can be translated.

**Parameter**

  * **language** (String) — The language and collation in which the names of the languages are returned. If this is `nil` then no names are returned. 



**Returns**

  * (Array<[Language](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-translate-v2/latest/Google-Cloud-Translate-V2-Language)>) — An array of [Language](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-translate-v2/latest/Google-Cloud-Translate-V2-Language "Google::Cloud::Translate::V2::Language \(class\)") objects supported by the API. 



**Examples**
    
    
    require "google/cloud/translate/v2"
    
    translate = Google::Cloud::Translate::V2.new
    
    languages = translate.languages
    languages.count #=> 104
    
    english = languages.detect { |l| l.code == "en" }
    english.name #=> nil

Get all languages with their names in French.
    
    
    require "google/cloud/translate/v2"
    
    translate = Google::Cloud::Translate::V2.new
    
    languages = translate.languages "fr"
    languages.count #=> 104
    
    english = languages.detect { |l| l.code == "en" }
    english.name #=> "Anglais"

### #project
    
    
    def project()

**Alias Of** : [#project_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-translate-v2/latest/Google-Cloud-Translate-V2-Api#Google__Cloud__Translate__V2__Api_project_id_instance_)

The Cloud Translation API project connected to.

**Example**
    
    
    require "google/cloud/translate/v2"
    
    translate = Google::Cloud::Translate::V2.new(
      project_id: "my-todo-project",
      credentials: "/path/to/keyfile.json"
    )
    
    translate.project_id #=> "my-todo-project"

### #project_id
    
    
    def project_id()

**Aliases**

  * [#project](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-translate-v2/latest/Google-Cloud-Translate-V2-Api#Google__Cloud__Translate__V2__Api_project_instance_)



The Cloud Translation API project connected to.

**Example**
    
    
    require "google/cloud/translate/v2"
    
    translate = Google::Cloud::Translate::V2.new(
      project_id: "my-todo-project",
      credentials: "/path/to/keyfile.json"
    )
    
    translate.project_id #=> "my-todo-project"

### #translate
    
    
    def translate(*text, to: nil, from: nil, format: nil, model: nil, cid: nil) -> Translation, Array<Translation>

Returns text translations from one language to another.

**Parameters**

  * **text** (String) — The text or texts to translate. 
  * **to** (String) _(defaults to: nil)_ — The target language into which the text should be translated. This is required. The value must be an [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language code. 
  * **from** (String) _(defaults to: nil)_ — The source language of the text or texts. This is an [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language code. This is optional. 
  * **format** (String) _(defaults to: nil)_ — The format of the text. Possible values include `:text` and `:html`. This is optional. The Translation API default is `:html`. 
  * **model** (String) _(defaults to: nil)_ — The model used by the service to perform the translation. Can be either `base` to use the Phrase-Based Machine Translation (PBMT) model, or `nmt` to use the Neural Machine Translation (NMT) model. The default is `nmt`.

If the model is `nmt`, and the requested language translation pair is not supported for the NMT model, then the request is translated using the PBMT model. 

  * **cid** (String) _(defaults to: nil)_ — The customization id for translate. This is optional. 



**Returns**

  * ([Translation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-translate-v2/latest/Google-Cloud-Translate-V2-Translation), Array<[Translation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-translate-v2/latest/Google-Cloud-Translate-V2-Translation)>) — A single [Translation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-translate-v2/latest/Google-Cloud-Translate-V2-Translation "Google::Cloud::Translate::V2::Translation \(class\)") object if just one text was given, or an array of [Translation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-translate-v2/latest/Google-Cloud-Translate-V2-Translation "Google::Cloud::Translate::V2::Translation \(class\)") objects if multiple texts were given. 



**Raises**

  * (ArgumentError) 



**Examples**
    
    
    require "google/cloud/translate/v2"
    
    translate = Google::Cloud::Translate::V2.new
    
    translation = translate.translate "Hello world!", to: "la"
    
    translation.to_s #=> "Salve mundi!"
    
    translation.detected? #=> true
    translation.from #=> "en"
    translation.origin #=> "Hello world!"
    translation.to #=> "la"
    translation.text #=> "Salve mundi!"
    translation.model #=> "base"

Using the neural machine translation model:
    
    
    require "google/cloud/translate/v2"
    
    translate = Google::Cloud::Translate::V2.new
    
    translation = translate.translate "Hello world!",
                                      to: "la", model: "nmt"
    
    translation.to_s #=> "Salve mundi!"
    translation.model #=> "nmt"

Setting the `from` language.
    
    
    require "google/cloud/translate/v2"
    
    translate = Google::Cloud::Translate::V2.new
    
    translation = translate.translate "Hello world!",
                                      from: :en, to: :la
    translation.detected? #=> false
    translation.text #=> "Salve mundi!"

Retrieving multiple translations.
    
    
    require "google/cloud/translate/v2"
    
    translate = Google::Cloud::Translate::V2.new
    
    translations = translate.translate "Hello my friend.",
                                       "See you soon.",
                                       from: "en", to: "la"
    translations.count #=> 2
    translations[0].text #=> "Salve amice."
    translations[1].text #=> "Vide te mox."

Preserving HTML tags.
    
    
    require "google/cloud/translate/v2"
    
    translate = Google::Cloud::Translate::V2.new
    
    translation = translate.translate "<strong>Hello</strong> world!",
                                      to: :la
    translation.text #=> "<strong>Salve</strong> mundi!"

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
