---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Translate
title: Interface Translate (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:27.531656+00:00
---

# Interface Translate (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Translate

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Translate (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.5  2.2.0  2.1.13 
    
    
    public interface Translate extends Service<TranslateOptions>

An interface for Google Translation. `Translate` and its `Option` classes can be used concurrently without external synchronizations. See Also: [Google Translation](https://cloud.google.com/translate/docs)

## Implements

com.google.cloud.Service<com.google.cloud.translate.TranslateOptions>

## Methods 

### detect(String text)
    
    
    public abstract Detection detect(String text)

Detects the language of the provided text. Returns an object containing information on the language detection.

Example of detecting the language of a text: 
    
    
     Detection detection = translate.detect("Hello, World!");
     

**Parameter**  
---  
**Name** | **Description**  
`text` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Detection](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Detection)` |   
  
### detect(String[] texts)
    
    
    public abstract List<Detection> detect(String[] texts)

Detects the language of the provided texts.

Example of detecting the language of some texts: 
    
    
     List<Detection> detections = translate.detect("Hello, World!", "¡Hola Mundo!");
     

**Parameter**  
---  
**Name** | **Description**  
`texts` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)[]`  
the texts for which language should be detected  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Detection](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Detection)>` | a list of objects containing information on the language detection, one for each provided text, in order  
  
### detect(List<String> texts)
    
    
    public abstract List<Detection> detect(List<String> texts)

Detects the language of the provided texts.

Example of detecting the language of some texts: 
    
    
     // TODO(developer): Uncomment these lines.
     // import com.google.cloud.translate.*;
     // Translate translate = TranslateOptions.getDefaultInstance().getService();
    
     List<String> texts = new LinkedList<>();
     texts.add("Hello, World!");
     texts.add("¡Hola Mundo!");
     List<Detection> detections = translate.detect(texts);
    
     System.out.println("Language(s) detected:");
     for (Detection detection : detections) {
       System.out.printf("  %s
    ", detection);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`texts` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
the texts for which language should be detected  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Detection](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Detection)>` | a list of objects containing information on the language detection, one for each provided text, in order  
  
### listSupportedLanguages(Translate.LanguageListOption[] options)
    
    
    public abstract List<Language> listSupportedLanguages(Translate.LanguageListOption[] options)

Returns the list of languages supported by Google Translation. If an option from [LanguageListOption#targetLanguage(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Translate.LanguageListOption#com_google_cloud_translate_Translate_LanguageListOption_targetLanguage_) is provided, the value of [Language#getName()](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Language#com_google_cloud_translate_Language_getName__) is localized according to the provided target language. If no such option is passed, the value of [Language#getName()](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Language#com_google_cloud_translate_Language_getName__) is localized according to [TranslateOptions#getTargetLanguage()](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.TranslateOptions#com_google_cloud_translate_TranslateOptions_getTargetLanguage__).

Example of listing supported languages, localized according to [TranslateOptions#getTargetLanguage()](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.TranslateOptions#com_google_cloud_translate_TranslateOptions_getTargetLanguage__): 
    
    
     // TODO(developer): Uncomment these lines.
     // import com.google.cloud.translate.*;
     // Translate translate = TranslateOptions.getDefaultInstance().getService();
    
     List<Language> languages = translate.listSupportedLanguages();
    
     for (Language language : languages) {
       System.out.printf("Name: %s, Code: %s
    ", language.getName(), language.getCode());
     }
     

Example of listing supported languages, localized according to a provided language: 
    
    
     // TODO(developer): Uncomment these lines.
     // import com.google.cloud.translate.*;
     // Translate translate = TranslateOptions.getDefaultInstance().getService();
    
     List<Language> languages = translate.listSupportedLanguages(
             Translate.LanguageListOption.targetLanguage("es"));
    
     for (Language language : languages) {
       System.out.printf("Name: %s, Code: %s
    ", language.getName(), language.getCode());
     }
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[LanguageListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Translate.LanguageListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Language](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Language)>` |   
  
### translate(String text, Translate.TranslateOption[] options)
    
    
    public abstract Translation translate(String text, Translate.TranslateOption[] options)

Translates the provided text.

Example of translating a text: 
    
    
     // TODO(developer): Uncomment these lines.
     // import com.google.cloud.translate.*;
     // Translate translate = TranslateOptions.getDefaultInstance().getService();
    
     Translation translation = translate.translate("¡Hola Mundo!");
     System.out.printf("Translated Text:
        %s
    ", translation.getTranslatedText());
     

Example of translating a text, specifying source and target language and premium model: 
    
    
     Translation translation = translate.translate(
         "Hola Mundo!",
         Translate.TranslateOption.sourceLanguage("es"),
         Translate.TranslateOption.targetLanguage("de"),
         // Use "base" for standard edition, "nmt" for the premium model.
         Translate.TranslateOption.model("nmt"));
    
     System.out.printf(
         "TranslatedText:
    Text: %s
    ",
         translation.getTranslatedText());
     

**Parameters**  
---  
**Name** | **Description**  
`text` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the text to translate  
`options` | `[TranslateOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Translate.TranslateOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Translation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Translation)` | an object containing information on the language translation  
  
### translate(List<String> texts, Translate.TranslateOption[] options)
    
    
    public abstract List<Translation> translate(List<String> texts, Translate.TranslateOption[] options)

Translates the provided texts.

Example of translating some texts: 
    
    
     List<String> texts = new LinkedList<>();
     texts.add("Hello, World!");
     texts.add("¡Hola Mundo!");
     List<Translation> translations = translate.translate(texts);
     

Example of translating some texts, specifying source and target language: 
    
    
     List<String> texts = new LinkedList<>();
     texts.add("¡Hola Mundo!");
     List<Translation> translations = translate.translate(
         texts,
         Translate.TranslateOption.sourceLanguage("es"),
         Translate.TranslateOption.targetLanguage("de"));
     

**Parameters**  
---  
**Name** | **Description**  
`texts` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
the texts to translate  
`options` | `[TranslateOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Translate.TranslateOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Translation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Translation)>` | a list of objects containing information on the language translation, one for each provided text, in order  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
