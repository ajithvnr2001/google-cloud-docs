---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/
title: Cloud Translation API - Package cloud.google.com/go/translate (v1.19.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:48.522201+00:00
---

# Cloud Translation API - Package cloud.google.com/go/translate (v1.19.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Cloud Translation API - Package cloud.google.com/go/translate (v1.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.19.0 (latest)  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.7  1.11.0  1.10.7  1.9.3  1.8.2  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.2.0  0.1.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/translate). 

Package translate is the v2 client for the Google Translation API. 

PLEASE NOTE: We recommend using the new v3 client for new projects: <https://cloud.google.com/go/translate/apiv3>. 

See <https://cloud.google.com/translation> for details.

##  Constants 

### Scope
    
    
    const Scope = raw.CloudPlatformScope

Scope is the OAuth2 scope required by the Google Cloud Vision API.

## Client
    
    
    type Client struct {
    	// contains filtered or unexported fields
    }

Client is a client for the translate API.

### func NewClient 
    
    
    func NewClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[option](https://pkg.go.dev/google.golang.org/api/option).[ClientOption](https://pkg.go.dev/google.golang.org/api/option#ClientOption)) (*Client, [error](https://pkg.go.dev/builtin#error))

NewClient constructs a new Client that can perform Translation operations.

You can find or create API key for your project from the Credentials page of the Developers Console (console.developers.google.com).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	"cloud.google.com/go/translate"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := translate.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/index.html#cloud_google_com_go_translate_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: handle error.
    	}
    	// Use the client.
    
    	// Close the client when finished.
    	if err := client.Close(); err != nil {
    		// TODO: handle error.
    	}
    }
    

### func (*Client) Close 
    
    
    func (c *Client) Close() [error](https://pkg.go.dev/builtin#error)

Close closes any resources held by the client. Close should be called when the client is no longer needed. It need not be called at program exit.

### func (*Client) DetectLanguage 
    
    
    func (c *Client) DetectLanguage(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), inputs [][string](https://pkg.go.dev/builtin#string)) ([][]Detection, [error](https://pkg.go.dev/builtin#error))

DetectLanguage attempts to determine the language of the inputs. Each input string may be in a different language.

Each slice of Detections in the return value corresponds with one input string. A slice of Detections holds multiple hypotheses for the language of a single input string.

#### Example
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/translate"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := translate.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/index.html#cloud_google_com_go_translate_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: handle error.
    	}
    	ds, err := client.DetectLanguage(ctx, []string{"Today is Monday"})
    	if err != nil {
    		// TODO: handle error.
    	}
    	fmt.Println(ds)
    }
    

### func (*Client) SupportedLanguages 
    
    
    func (c *Client) SupportedLanguages(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), target [language](https://pkg.go.dev/golang.org/x/text/language).[Tag](https://pkg.go.dev/golang.org/x/text/language#Tag)) ([]Language, [error](https://pkg.go.dev/builtin#error))

SupportedLanguages returns a list of supported languages for translation. The target parameter is the language to use to return localized, human readable names of supported languages.

#### Example
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/translate"
    	"golang.org/x/text/language"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := translate.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/index.html#cloud_google_com_go_translate_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: handle error.
    	}
    	langs, err := client.SupportedLanguages(ctx, language.English)
    	if err != nil {
    		// TODO: handle error.
    	}
    	fmt.Println(langs)
    }
    

### func (*Client) Translate 
    
    
    func (c *Client) Translate(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), inputs [][string](https://pkg.go.dev/builtin#string), target [language](https://pkg.go.dev/golang.org/x/text/language).[Tag](https://pkg.go.dev/golang.org/x/text/language#Tag), opts *Options) ([]Translation, [error](https://pkg.go.dev/builtin#error))

Translate one or more strings of text from a source language to a target language. All inputs must be in the same language.

The target parameter supplies the language to translate to. The supported languages are listed at <https://cloud.google.com/translation/v2/translate-reference#supported_languages>. You can also call the SupportedLanguages method.

The returned Translations appear in the same order as the inputs.

#### Example
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/translate"
    	"golang.org/x/text/language"
    )
    
    func main() {
    	ctx := context.Background()
    	client, err := translate.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/index.html#cloud_google_com_go_translate_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: handle error.
    	}
    	translations, err := client.[Translate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/index.html#cloud_google_com_go_translate_Client_Translate)(ctx,
    		[]string{"Le singe est sur la branche"}, language.English,
    		&translate.[Options](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/index.html#cloud_google_com_go_translate_Options){
    			Source: language.French,
    			Format: translate.[Text](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/index.html#cloud_google_com_go_translate_HTML_Text),
    		})
    	if err != nil {
    		// TODO: handle error.
    	}
    	fmt.Println(translations[0].[Text](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/index.html#cloud_google_com_go_translate_HTML_Text))
    }
    

## Detection
    
    
    type Detection struct {
    	// Language is the code of the language detected.
    	Language language.Tag
    
    	// Confidence is a number from 0 to 1, with higher numbers indicating more
    	// confidence in the detection.
    	Confidence [float64](https://pkg.go.dev/builtin#float64)
    
    	// IsReliable indicates whether the language detection result is reliable.
    	IsReliable [bool](https://pkg.go.dev/builtin#bool)
    }

Detection represents information about a language detected in an input.

## Format
    
    
    type Format [string](https://pkg.go.dev/builtin#string)

Format is the format of the input text. Used in Options.Format.

### HTML, Text
    
    
    const (
    	HTML Format = "html"
    	Text Format = "text"
    )

Constants for Options.Format.

## Language
    
    
    type Language struct {
    	// Name is the human-readable name of the language.
    	Name [string](https://pkg.go.dev/builtin#string)
    
    	// Tag is a standard code for the language.
    	Tag language.Tag
    }

A Language describes a language supported for translation.

## Options
    
    
    type Options struct {
    	// Source is the language of the input strings. If empty, the service will
    	// attempt to identify the source language automatically and return it within
    	// the response.
    	Source language.Tag
    
    	// Format describes the format of the input texts. The choices are HTML or
    	// Text. The default is HTML.
    	Format Format
    
    	// The model to use for translation. The choices are "nmt" or "base". The
    	// default is "base".
    	Model [string](https://pkg.go.dev/builtin#string)
    }

Options contains options for Translate.

## Translation
    
    
    type Translation struct {
    	// Text is the input text translated into the target language.
    	Text [string](https://pkg.go.dev/builtin#string)
    
    	// Source is the detected language of the input text, if source was
    	// not supplied to Client.Translate. If source was supplied, this field
    	// will be empty.
    	Source language.Tag
    
    	// Model is the model that was used for translation.
    	// It may not match the model provided as an option to Client.Translate.
    	Model [string](https://pkg.go.dev/builtin#string)
    }

Translation contains the results of translating a piece of text.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
