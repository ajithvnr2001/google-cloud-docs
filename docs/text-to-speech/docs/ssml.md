---
url: https://docs.cloud.google.com/text-to-speech/docs/ssml/
title: Speech Synthesis Markup Language (SSML) \u00a0|\u00a0 Cloud Text-to-Speech \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:19.951270+00:00
---

# Speech Synthesis Markup Language (SSML)  |  Cloud Text-to-Speech  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/text-to-speech/docs/ssml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Text-to-Speech ](https://docs.cloud.google.com/text-to-speech/docs)
  * [ Reference ](https://docs.cloud.google.com/text-to-speech/docs/apis)



Send feedback 

#  Speech Synthesis Markup Language (SSML) Stay organized with collections  Save and categorize content based on your preferences. 

You can send [Speech Synthesis Markup Language (SSML)](https://www.w3.org/TR/speech-synthesis/) in your Cloud Text-to-Speech request to allow for more customization in your audio response by providing details on pauses, and audio formatting for acronyms, dates, times, abbreviations, or text that should be censored. See the Cloud TTS [SSML tutorial](https://docs.cloud.google.com/text-to-speech/docs/ssml-tutorial) for more information and code samples.

**Note:** SSML characters count toward character limits. See the [quotas & limits](https://docs.cloud.google.com/text-to-speech/quotas) page for more information.

The following shows an example of SSML markup and the Cloud TTS synthesizes the text:
    
    
    <speak>
      Here are <say-as interpret-as="characters">SSML</say-as> samples.
      I can pause <break time="3s"/>.
      I can play a sound
      <audio src="https://www.example.com/MY_MP3_FILE.mp3">didn't get your MP3 audio file</audio>.
      I can speak in cardinals. Your number is <say-as interpret-as="cardinal">10</say-as>.
      Or I can speak in ordinals. You are <say-as interpret-as="ordinal">10</say-as> in line.
      Or I can even speak in digits. The digits for ten are <say-as interpret-as="characters">10</say-as>.
      I can also substitute phrases, like the <sub alias="World Wide Web Consortium">W3C</sub>.
      Finally, I can speak a paragraph with two sentences.
      <p><s>This is sentence one.</s><s>This is sentence two.</s></p>
    </speak>

Here is the synthesized text for the example SSML document:
    
    
    Here are S S M L samples. I can pause [3 second pause]. I can play a sound [audio file plays].
    I can speak in cardinals. Your number is ten.
    Or I can speak in ordinals. You are tenth in line.
    Or I can even speak in digits. The digits for ten are one oh.
    I can also substitute phrases, like the World Wide Web Consortium.
    Finally, I can speak a paragraph with two sentences. This is sentence one. This is sentence two.

The Cloud TTS supports a subset of the available SSML tags, which are described in this topic.

**Note:** You can practice using SSML tags using the Text-to-Speech product demo on the [product overview](https://cloud.google.com/text-to-speech) page. Click the **ssml** link under the bottom right corner of the "Convert your text to speech right now" demo's text box to view your input in ssml format.

For more information about how to create audio data from SSML input with the Cloud TTS, see [Creating Voice Audio Files](https://docs.cloud.google.com/text-to-speech/docs/create-audio#ssml).

##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud TTS performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud TTS free ](https://console.cloud.google.com/freetrial)

## Tips for using SSML

Depending on your implementation, you may need to escape quotation marks or quotes in the SSML payload that you send to Cloud TTS. The following example shows how to format SSML input included within a JSON object.
    
    
    "{
        'input':{
         'ssml':'<speak>The <say-as interpret-as=\"characters\">SSML</say-as>
              standard <break time=\"1s\"/>is defined by the
              <sub alias=\"World Wide Web Consortium\">W3C</sub>.</speak>'
        },
        'voice':{
          'languageCode':'en-us',
          'name':'en-US-Standard-B',
          'ssmlGender':'MALE'
        },
        'audioConfig':{
          'audioEncoding':'MP3'
        }
      }"

### Reserve characters

Avoid using SSML reserve characters in the text that is to be converted to audio. When you need to use an SSML reserve character, prevent the character from being read as code by using its escape code. The following table shows reserved SSML characters and their associated escape codes.

Character | Escape code  
---|---  
" | `&quot;`  
& | `&amp;`  
' | `&apos;`  
< | `&lt;`  
> | `&gt;`  
  
### Select a voice

You can set the voice in the [`VoiceSelectionParams`](https://docs.cloud.google.com/text-to-speech/docs/reference/rest/v1/text/synthesize#voiceselectionparams) object. See the Text-to-Speech [SSML tutorial](https://docs.cloud.google.com/text-to-speech/docs/ssml-tutorial) to see a [code sample](https://docs.cloud.google.com/text-to-speech/docs/ssml-tutorial#using_api) demonstrating use of the `VoiceSelectionParams` object.

You can use the `<voice>` tag to read SSML in multiple voices, but you must set the `VoiceSelectionParams` name to a compatible voice:

Requested voice type | Supported voice type in <voice> tag  
---|---  
Neural2 | Studio | Wavenet | News | Standard  
Neural2 | ✔ | ✔ |  |  | ✔  
Studio | ✔ | ✔ |  |  | ✔  
Wavenet |  |  | ✔ | ✔ | ✔  
Standard | ✔ | ✔ |  |  | ✔  
News |  |  | ✔ | ✔ | ✔  
  
## Support for SSML elements

The following sections describe the SSML elements and options that can be used in your Actions.

Note that not all of the elements and options described in the [W3 SSML specification](https://www.w3.org/TR/speech-synthesis/) are currently supported by Cloud Text-to-Speech. This page details which elements and options are available for your application. The W3 reference links provided below may be helpful for additional context and examples.

## `<speak>`

The root element of the SSML response.

To learn more about the `speak` element, see the [W3 specification](https://www.w3.org/TR/speech-synthesis/#edef_speak).

### Example
    
    
    <speak>
      my SSML content
    </speak>

Your browser does not support the HTML5 Audio element.

## `<break>`

An empty element that controls pausing or other prosodic boundaries between words. Using `<break>` between any pair of tokens is optional. If this element is not present between words, the break is automatically determined based on the linguistic context.

To learn more about the `break` element, see the [W3 specification](https://www.w3.org/TR/speech-synthesis/#S3.2.3).

### Attributes

Attribute | Description  
---|---  
`time` | Sets the length of the break by seconds or milliseconds (e.g. "3s" or "250ms").  
`strength` | Sets the strength of the output's prosodic break by relative terms. Valid values are: "x-weak", weak", "medium", "strong", and "x-strong". The value "none" indicates that no prosodic break boundary should be outputted, which can be used to prevent a prosodic break that the processor would otherwise produce. The other values indicate monotonically non-decreasing (conceptually increasing) break strength between tokens. The stronger boundaries are typically accompanied by pauses.  
  
### Example

The following example shows how to use the `<break>` element to pause between steps:
    
    
    <speak>
      Step 1, take a deep breath. <break time="200ms"/>
      Step 2, exhale.
      Step 3, take a deep breath again. <break strength="weak"/>
      Step 4, exhale.
    </speak>

Your browser does not support the HTML5 Audio element.

## `<say‑as>`

This element lets you indicate information about the type of text construct that is contained within the element. It also helps specify the level of detail for rendering the contained text.

The `<say‑as>` element has the required attribute, `interpret-as`, which determines how the value is spoken. Optional attributes `format` and `detail` may be used depending on the particular `interpret-as` value.

### Examples

The `interpret-as` attribute supports the following values:

  * `currency`

The following example is spoken as "forty two dollars and one cent". If the language attribute is omitted, it uses the current locale.
        
        <speak>
          <say-as interpret-as='currency' language='en-US'>$42.01</say-as>
        </speak>
            

  * `telephone`

See the `interpret-as='telephone'` description in the W3C SSML 1.0 [say-as attribute values](https://www.w3.org/TR/ssml-sayas/#S3.3) WG note.

The following example is spoken as "one eight zero zero two zero two one two one two". If the "google:style" attribute is omitted, it speaks zero as letter O.

The "google:style='zero-as-zero'" attribute currently only works in EN locales.
        
        <speak>
                <say-as interpret-as='telephone' google:style='zero-as-zero'>1800-202-1212</say-as>
              </speak>
            

  * `verbatim` or `spell-out`

The following example is spelled out letter by letter:
        
        <speak>
          <say-as interpret-as="verbatim">abcdefg</say-as>
        </speak>
            

Your browser does not support the HTML5 Audio element.

  * `date`

The `format` attribute is a sequence of date field character codes. Supported field character codes in `format` are {`y`, `m`, `d`} for year, month, and day (of the month) respectively. If the field code appears once for year, month, or day then the number of digits expected are 4, 2, and 2 respectively. If the field code is repeated then the number of expected digits is the number of times the code is repeated. Fields in the date text may be separated by punctuation and/or spaces.

The `detail` attribute controls the spoken form of the date. For `detail='1'` only the day fields and one of month or year fields are required, although both may be supplied. This is the default when less than all three fields are given. The spoken form is "The {ordinal day} of {month}, {year}".

The following example is spoken as "The tenth of September, nineteen sixty":
        
        <speak>
          <say-as interpret-as="date" format="yyyymmdd" detail="1">
            1960-09-10
          </say-as>
        </speak>
            

Your browser does not support the HTML5 Audio element.

The following example is spoken as "The tenth of September":
        
        <speak>
          <say-as interpret-as="date" format="dm">10-9</say-as>
        </speak>
            

Your browser does not support the HTML5 Audio element.

For `detail='2'` the day, month, and year fields are required and this is the default when all three fields are supplied. The spoken form is "{month} {ordinal day}, {year}".

The following example is spoken as "September tenth, nineteen sixty":
        
        <speak>
          <say-as interpret-as="date" format="dmy" detail="2">
            10-9-1960
          </say-as>
        </speak>
            

Your browser does not support the HTML5 Audio element.

  * `characters`

The following example is spoken as "C A N":
        
        <speak>
          <say-as interpret-as="characters">can</say-as>
        </speak>
            

Your browser does not support the HTML5 Audio element.

  * `cardinal`

The following example is spoken as "Twelve thousand three hundred forty five" (for US English) or "Twelve thousand three hundred and forty five (for UK English)":
        
        <speak>
          <say-as interpret-as="cardinal">12345</say-as>
        </speak>
            

Your browser does not support the HTML5 Audio element.

  * `ordinal`

The following example is spoken as "First":
        
        <speak>
          <say-as interpret-as="ordinal">1</say-as>
        </speak>
            

Your browser does not support the HTML5 Audio element.

  * `fraction`

The following example is spoken as "five and a half":
        
        <speak>
          <say-as interpret-as="fraction">5+1/2</say-as>
        </speak>
            

Your browser does not support the HTML5 Audio element.

  * `expletive` or `bleep`

The following example comes out as a beep, as though it has been censored:
        
        <speak>
          <say-as interpret-as="expletive">censor this</say-as>
        </speak>
            

Your browser does not support the HTML5 Audio element.

  * `unit`

Converts units to singular or plural depending on the number. The following example is spoken as "10 feet":
        
        <speak>
          <say-as interpret-as="unit">10 foot</say-as>
        </speak>
            

Your browser does not support the HTML5 Audio element.

  * `time`

The following example is spoken as "Two thirty P.M.":
        
        <speak>
          <say-as interpret-as="time" format="hms12">2:30pm</say-as>
        </speak>
            

Your browser does not support the HTML5 Audio element.

The `format` attribute is a sequence of time field character codes. Supported field character codes in `format` are {`h`,`m`, `s`, `Z`, `12`, `24`} for hour, minute (of the hour), second (of the minute), time zone, 12-hour time, and 24-hour time respectively. If the field code appears once for hour, minute, or second then the number of digits expected are 1, 2, and 2 respectively. If the field code is repeated then the number of expected digits is the number of times the code is repeated. Fields in the time text may be separated by punctuation and/or spaces. If hour, minute, or second are not specified in the format or there are no matching digits then the field is treated as a zero value. The default `format` is "hms12".

The `detail` attribute controls whether the spoken form of the time is 12-hour time or 24-hour time. The spoken form is 24-hour time if `detail='1'` or if `detail` is omitted and the format of the time is 24-hour time. The spoken form is 12-hour time if `detail='2'` or if `detail` is omitted and the format of the time is 12-hour time.




To learn more about the `say-as` element, see the [W3 specification](https://www.w3.org/TR/speech-synthesis/#S3.1.9).

## `<audio>`

Supports the insertion of recorded audio files and the insertion of other audio formats in conjunction with synthesized speech output.

### Attributes

Attribute | Required | Default | Values  
---|---|---|---  
`src` | yes | n/a | A URI referring to the audio media source. Supported protocol is `https`.  
`clipBegin` | no | 0 | A [TimeDesignation](https://www.w3.org/TR/speech-synthesis11/#def_time_designation) that is the offset from the audio source's beginning to start playback from. If this value is greater than or equal to the audio source's actual duration, then no audio is inserted.  
`clipEnd` | no | infinity | A [TimeDesignation](https://www.w3.org/TR/speech-synthesis11/#def_time_designation) that is the offset from the audio source's beginning to end playback at. If the audio source's actual duration is less than this value, then playback ends at that time. If `clipBegin` is greater than or equal to `clipEnd`, then no audio is inserted.  
`speed` | no | 100% | The ratio output playback rate relative to the normal input rate expressed as a percentage. The format is a positive [Real Number](https://www.w3.org/TR/speech-synthesis11/#def_real_number) followed by %. The currently supported range is [50% (slow - half speed), 200% (fast - double speed)]. Values outside that range may (or may not) be adjusted to be within it.  
`repeatCount` | no | 1, or 10 if `repeatDur` is set | A [Real Number](https://www.w3.org/TR/speech-synthesis11/#def_real_number) specifying how many times to insert the audio (after clipping, if any, by `clipBegin` and/or `clipEnd`). Fractional repetitions aren't supported, so the value will be rounded to the nearest integer. Zero is not a valid value and is therefore treated as being unspecified and has the default value in that case.  
`repeatDur` | no | infinity | A [TimeDesignation](https://www.w3.org/TR/speech-synthesis11/#def_time_designation) that is a limit on the duration of the inserted audio after the source is processed for `clipBegin`, `clipEnd`, `repeatCount`, and `speed` attributes (rather then the normal playback duration). If the duration of the processed audio is less than this value, then playback ends at that time.  
`soundLevel` | no | +0dB | Adjust the sound level of the audio by `soundLevel`decibels. Maximum range is +/-40dB but actual range may be effectively less, and output quality may not yield good results over the entire range.  
  
The following are the currently supported settings for audio:

  * Format: MP3 (MPEG v2) 
    * 24K samples per second
    * 24K ~ 96K bits per second, fixed rate
  * Format: Opus in Ogg 
    * 24K samples per second (super-wideband)
    * 24K - 96K bits per second, fixed rate
  * Format (deprecated): WAV (RIFF) 
    * PCM 16-bit signed, little endian
    * 24K samples per second
  * For all formats: 
    * Single channel is preferred, but stereo is acceptable.
    * 240 seconds maximum duration. If you want to play audio with a longer duration, consider implementing a [media response](https://developers.google.com/actions/assistant/responses#media_responses).
    * 5 megabyte file size limit.
    * Source URL must use HTTPS protocol.
    * Our UserAgent when fetching the audio is "Google-Speech-Actions".



The contents of the `<audio>` element are optional and are used if the audio file cannot be played or if the output device does not support audio. The contents may include a `<desc>` element in which case the text contents of that element are used for display. For more information, see the Recorded Audio section in the [Responses Checklist](https://developers.google.com/actions/assistant/responses#ui_checklist).

The `src` URL must also be an https URL ([Google Cloud Storage](https://cloud.google.com/storage/docs/creating-buckets) can host your audio files on an https URL).

To learn more about media responses, see the [media response](https://developers.google.com/actions/assistant/responses#media_responses) section in the Responses guide.

To learn more about the `audio` element, see the [W3 specification](https://www.w3.org/TR/speech-synthesis/#S3.3.1).

### Example
    
    
    <speak>
      <audio src="cat_purr_close.ogg">
        <desc>a cat purring</desc>
        PURR (sound didn't load)
      </audio>
    </speak>

Your browser does not support the HTML5 Audio element.

## `<p>,<s>`

Sentence and paragraph elements.

To learn more about the `p` and `s` elements, see the [W3 specification](https://www.w3.org/TR/speech-synthesis/#edef_paragraph).

### Example
    
    
    <p><s>This is sentence one.</s><s>This is sentence two.</s></p>

Your browser does not support the HTML5 Audio element.

### Best practices

  * Use <s>...</s> tags to wrap full sentences, especially if they contain SSML elements that change prosody (that is, <audio>, <break>, <emphasis>, <par>, <prosody>, <say-as>, <seq>, and <sub>).
  * If a break in speech is intended to be long enough that you can hear it, use <s>...</s> tags and put that break between sentences.



## `<sub>`

Indicate that the text in the alias attribute value replaces the contained text for pronunciation.

You can also use the `sub` element to provide a simplified pronunciation of a difficult-to-read word. The last example below demonstrates this use case in Japanese.

To learn more about the `sub` element, see the [W3 specification](https://www.w3.org/TR/speech-synthesis/#edef_sub).

### Examples
    
    
    <sub alias="World Wide Web Consortium">W3C</sub>

Your browser does not support the HTML5 Audio element.
    
    
    <sub alias="にっぽんばし">日本橋</sub>

Your browser does not support the HTML5 Audio element.

## `<mark>`

An empty element that places a marker into the text or tag sequence. It can be used to reference a specific location in the sequence or to insert a marker into an output stream for asynchronous notification.

**Note:** Follow these guidelines when you use the `mark` element: 

  * Use the `START` and `END` marks instead of adding custom marks near the beginning or end of the SSML.
  * Do not add consecutive marks in your SSML. Marks in rapid succession might not generate events. Additionally, if there is no audio generated between marks, then events won't be generated. For example, avoid doing the following:   
`Sentence 1. `<mark name=a><mark name=b>` Sentence 2.`   


**Note:** For convenience, you automatically get `START` and `END` events in your responses for [Interactive Canvas](https://developers.google.com/assistant/interactivecanvas). These marks are not included in the W3 spec. Attribute | Description  
---|---  
`name` | The string ID for each mark.  
  
To learn more about the `mark` element, see the [W3 specification](https://www.w3.org/TR/speech-synthesis/#S3.3.2).

### Example
    
    
    <speak>
    Go from <mark name="here"/> here, to <mark name="there"/> there!
    </speak>

Your browser does not support the HTML5 Audio element.

## `<prosody>`

Used to customize the pitch, speaking rate, and volume of text contained by the element. Currently the `rate`, `pitch`, and `volume` attributes are supported.

The `rate` and `volume` attributes can be set according to the [W3 specifications](https://www.w3.org/TR/speech-synthesis11/#S3.2.4). There are three options for setting the value of the `pitch` attribute:

**Note:** The `<prosody>` tags should only be used around a full sentence. Enclosing words within a sentence may cause unwanted pauses in speech.Option | Description  
---|---  
Relative | Specify a relative value (e.g. "low", "medium", "high", etc) where "medium" is the default pitch.  
Semitones | Increase or decrease pitch by "**N** " semitones using "+**N** st" or "-**N** st" respectively. Note that "+/-" and "st" are required.  
Percentage | Increase or decrease pitch by "**N** " percent by using "+**N** %" or "-**N** %" respectively. Note that "%" is required but "+/-" is optional.  
  
To learn more about the `prosody` element, see the [W3 specification](https://www.w3.org/TR/speech-synthesis11/#S3.2.4).

### Example

The following example uses the `<prosody>` element to speak slowly at 2 semitones lower than normal:
    
    
    <prosody rate="slow" pitch="-2st">Can you hear me now?</prosody>

Your browser does not support the HTML5 Audio element.

## `<emphasis>`

Used to add or remove emphasis from text contained by the element. The `<emphasis>` element modifies speech similarly to `<prosody>`, but without the need to set individual speech attributes.

**Note:** The `<emphasis>` tags should only be used around a full sentence. Enclosing words within a sentence may cause unwanted pauses in speech.

This element supports an optional "level" attribute with the following valid values:

  * `strong`
  * `moderate`
  * `none`
  * `reduced`



To learn more about the `emphasis` element, see the [W3 specification](https://www.w3.org/TR/speech-synthesis11/#S3.2.2).

### Example

The following example uses the `<emphasis>` element to make an announcement:
    
    
    <emphasis level="moderate">This is an important announcement</emphasis>

Your browser does not support the HTML5 Audio element.

## `<par>`

A parallel media container that allows you to play multiple media elements at once. The only allowed content is a set of one or more `<par>`, `<seq>`, and `<media>` elements. The order of the `<media>` elements is not significant.

Unless a child element specifies a different begin time, the implicit begin time for the element is the same as that of the `<par>` container. If a child element has an offset value set for its **begin** or **end** attribute, the element's offset will be relative to the beginning time of the `<par>` container. For the root `<par>` element, the begin attribute is ignored and the beginning time is when SSML speech synthesis process starts generating output for the root `<par>` element (i.e. effectively time "zero").

Note: This element is not a standard SSML element and is provided as an extra feature of Cloud Text-to-Speech.

### Example
    
    
    <speak>
      <par>
        <media xml:id="question" begin="0.5s">
          <speak>Who invented the Internet?</speak>
        </media>
        <media xml:id="answer" begin="question.end+2.0s">
          <speak>The Internet was invented by cats.</speak>
        </media>
        <media begin="answer.end-0.2s" soundLevel="-6dB">
          <audio
            src="https://actions.google.com/.../cartoon_boing.ogg"/>
        </media>
        <media repeatCount="3" soundLevel="+2.28dB"
          fadeInDur="2s" fadeOutDur="0.2s">
          <audio
            src="https://actions.google.com/.../cat_purr_close.ogg"/>
        </media>
      </par>
    </speak>

Your browser does not support the HTML5 Audio element.

## `<seq>`

A sequential media container that allows you to play media elements one after another. The only allowed content is a set of one or more `<seq>`, `<par>`, and `<media>` elements. The order of the media elements is the order in which they are rendered.

The **begin** and **end** attributes of child elements can be set to offset values (see **Time Specification** below). Those child elements' offset values will be relative to the end of the previous element in the sequence or, in the case of the first element in the sequence, relative to the beginning of its `<seq>` container.

Note: This element is not a standard SSML element and is provided as an extra feature of Cloud Text-to-Speech.

### Example
    
    
    <speak>
      <seq>
        <media begin="0.5s">
          <speak>Who invented the Internet?</speak>
        </media>
        <media begin="2.0s">
          <speak>The Internet was invented by cats.</speak>
        </media>
        <media soundLevel="-6dB">
          <audio
            src="https://actions.google.com/.../cartoon_boing.ogg"/>
        </media>
        <media repeatCount="3" soundLevel="+2.28dB"
          fadeInDur="2s" fadeOutDur="0.2s">
          <audio
            src="https://actions.google.com/.../cat_purr_close.ogg"/>
        </media>
      </seq>
    </speak>

Your browser does not support the HTML5 Audio element.

## `<media>`

Represents a media layer within a `<par>` or `<seq>` element. The allowed content of a `<media>` element is an SSML `<speak>` or `<audio>` element. The following table describes the valid attributes for a `<media>` element.

Note: This element is not a standard SSML element and is provided as an extra feature of the Actions on Google platform.

### Attributes

Attribute | Required | Default | Values  
---|---|---|---  
**xml:id** | no | no value | A unique XML identifier for this element. Encoded entities are not supported. The allowed identifier values match the regular expression `"([-_#]|\p{L}|\p{D})+"`. See [XML-ID](http://www.w3.org/TR/xml-id/) for more information.  
**begin** | no | 0 | The beginning time for this media container. Ignored if this is the root media container element (treated the same as the default of "0"). See the **Time specification** section below for valid string values.  
**end** | no | no value | A specification for the ending time for this media container. See the **Time specification** section below for valid string values.  
**repeatCount** | no | 1 | A [Real Number](https://www.w3.org/TR/speech-synthesis11/#def_real_number) specifying how many times to insert the media. Fractional repetitions aren't supported, so the value will be rounded to the nearest integer. Zero is not a valid value and is therefore treated as being unspecified and has the default value in that case.  
**repeatDur** | no | no value | A [TimeDesignation](https://www.w3.org/TR/speech-synthesis11/#def_time_designation) that is a limit on the duration of the inserted media. If the duration of the media is less than this value, then playback ends at that time.  
**soundLevel** | no | +0dB | Adjust the sound level of the audio by `soundLevel` decibels. Maximum range is +/-40dB but actual range may be effectively less, and output quality may not yield good results over the entire range.  
**fadeInDur** | no | 0s | A [TimeDesignation](https://www.w3.org/TR/speech-synthesis11/#def_time_designation) over which the media will fade in from silent to the optionally-specified `soundLevel`. If the duration of the media is less than this value, the fade in will stop at the end of playback and the sound level will not reach the specified sound level.  
**fadeOutDur** | no | 0s | A [TimeDesignation](https://www.w3.org/TR/speech-synthesis11/#def_time_designation) over which the media will fade out from the optionally-specified `soundLevel` until it is silent. If the duration of the media is less than this value, the sound level is set to a lower value to ensure silence is reached at the end of playback.  
  
### Time specification

A time specification, used for the value of `begin` and `end` attributes of `<media>` elements and media containers (`<par>` and `<seq>` elements), is either an offset value (for example, `+2.5s`) or a syncbase value (for example, `foo_id.end-250ms`).

  * **Offset value** \- Time offset value is an SMIL Timecount-value that allows values that match the regular expression: `"\s\*(+|-)?\s\*(\d+)(\.\d+)?(h|min|s|ms)?\s\*"`

The first digit string is the whole part of the decimal number and the second digit string is the decimal fractional part. The default sign (i.e. "(+|-)?") is "+". The unit values correspond to hours, minutes, seconds, and milliseconds respectively. The default for the units is "s" (seconds).

  * **Syncbase value** \- A syncbase value is an SMIL syncbase-value that allows values that match the regular expression: `"([-_#]|\p{L}|\p{D})+\.(begin|end)\s\*(+|-)\s\*(\d+)(\.\d+)?(h|min|s|ms)?\s\*"`

The digits and units are interpreted in the same way as an offset value.




## `<phoneme>`

You can use the `<phoneme>` tag to produce custom pronunciations of words inline. Cloud TTS accepts the [IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) and [X-SAMPA](https://en.wikipedia.org/wiki/X-SAMPA) phonetic alphabets. See the [phonemes page](https://docs.cloud.google.com/text-to-speech/docs/phonemes) for a list of supported languages and phonemes.

Each application of the `<phoneme>` tag directs the pronunciation of a single word:
    
    
      <phoneme alphabet="ipa" ph="ˌmænɪˈtoʊbə">manitoba</phoneme>
      <phoneme alphabet="x-sampa" ph='m@"hA:g@%ni:'>mahogany</phoneme>

**Note:** Set the `alphabet` field to either `ipa` or `x-sampa`, depending on which phonetic alphabet you're using. The only exceptions are Japanese, which must be specified as `yomigana`, and the Chinese languages, which must be specified as `pinyin` or `jyutping`. See the [phonemes page](https://docs.cloud.google.com/text-to-speech/docs/phonemes) to see which phonetic alphabets are available for you language.

### Stress markers

There are up to three levels of stress that can be placed in a transcription:

  1. **Primary stress** : Denoted with /ˈ/ in IPA and /"/ in X-SAMPA.
  2. **Secondary stress** : Denoted with /ˌ/ in IPA and /%/ in X-SAMPA.
  3. **Unstressed** : Not denoted with a symbol (in either notation).



Some languages might have fewer than three levels or not denote stress placement at all. See the [phonemes page](https://docs.cloud.google.com/text-to-speech/docs/phonemes) to see the stress levels available for your language. Stress markers are placed at the start of each stressed syllable. For example, in US English:

Example word | IPA | X-SAMPA  
---|---|---  
water | ˈwɑːtɚ | "wA:t@`  
underwater | ˌʌndɚˈwɑːtɚ | %Vnd@"wA:t@  
  
### Broad vs Narrow Transcriptions

As a general rule, keep your transcriptions more broad and phonemic in nature. For example, in US English, transcribe intervocalic /t/ (instead of using a tap):

Example word | IPA | X-SAMPA  
---|---|---  
butter | ˈbʌtɚ instead of ˈbʌɾɚ | "bVt@` instead of "bV4@`  
  
There are some instances where using the phonemic representation makes your TTS results sound unnatural (for example, if the sequence of phonemes is anatomically difficult to pronounce).

One example of this is voicing assimilation for /s/ in English. In this case the assimilation should be reflected in the transcription:

Example word | IPA | X-SAMPA  
---|---|---  
cats | ˈkæts | "k{ts  
dogs | ˈdɑːgz instead of ˈdɑːgs | "dA:gz instead of "dA:gs  
  
### Reduction

Every syllable must contain one (and only one) vowel. This means that you should avoid syllabic consonants and instead transcribe them with a reduced vowel. For example:

Example word | IPA | X-SAMPA  
---|---|---  
kitten | ˈkɪtən instead of ˈkɪtn | "kIt@n instead of "kitn  
kettle | ˈkɛtəl instead of ˈkɛtl | "kEt@l instead of "kEtl  
  
### Syllabification

You can optionally specify syllable boundaries by using /./. Each syllable must contain one (and only one) vowel. For example:

Example word | IPA | X-SAMPA  
---|---|---  
readability | ˌɹiː.də.ˈbɪ.lə.tiː | %r\i:.d@."bI.l@.ti:  
  
### Custom pronunciation dictionary

As an alternative to providing pronunciations inline with the `phoneme` tag, provide a dictionary of custom pronunciations in the speech synthesis RPC. When the custom pronunciation dictionary is in the request, the input text will automatically be transformed with the SSML `phoneme` tag.

As an example, the following request with text input and custom pronunciation will be transformed and will be equivalent to the SSML below.

Original Input:
    
    
    input: {
      text: 'Hello world! It is indeed a beautiful world!',
      custom_pronunciations: {
        pronunciations: {
          phrase: 'world'
          phonetic_encoding: PHONETIC_ENCODING_IPA
          pronunciation: 'wɜːld'
        }
      }
    }

Transformed input:
    
    
    input: {
      ssml: '<speak>Hello <phoneme alphabet="ipa" ph="wɜːld">world</phoneme>! It is indeed a beautiful <phoneme alphabet="ipa" ph="wɜːld">world</phoneme>!</speak>'
    }

## Durations

Cloud Text-to-Speech supports `<say-as interpret-as="duration">` to correctly read durations. For example, the following example would be verbalized as "five hours and thirty minutes":
    
    
    <say-as interpret-as="duration" format="h:m">5:30</say-as>

The format string supports the following values:

Abbreviation | Value  
---|---  
h | hours  
m | minutes  
s | seconds  
ms | milliseconds  
  
## `<voice>`

The `<voice>` tag allows you to use more than one voice in a single SSML request. In the following example, the default voice is an English male voice. All words will be synthesized in this voice except for "qu'est-ce qui t'amène ici", which will be verbalized in French using a female voice instead of the default language (English) and gender (male). 
    
    
    <speak>And then she asked, <voice language="fr-FR" gender="female">qu'est-ce qui
    t'amène ici</voice><break time="250ms"/> in her sweet and gentle voice.</speak>

Alternatively, you can use a `<voice>` tag to specify an individual voice (the **voice name** on the [supported voices page](https://docs.cloud.google.com/text-to-speech/docs/voices)) rather than specifying a `language` and/or `gender`:
    
    
    <speak>The dog is friendly<voice name="fr-CA-Wavenet-B">mais la chat est
    mignon</voice><break time="250ms"/> said a pet shop
    owner</speak>

**Note:** When a `<voice>` tag specifies a voice name, the type of voice must be compatible with the requested voice name.

When you use the `<voice>` tag, Cloud TTS expects to receive either a `name` (the [name of the voice](https://docs.cloud.google.com/text-to-speech/docs/voices) you want to use) **or** a combination of the following attributes. All three attributes are optional but you must provide at least one if you don't provide a `name`.

  * `gender`: One of "male", "female" or "neutral".
  * `variant`: Used as a tiebreaker in cases where there are multiple possibilities of which voice to use based on your configuration.
  * `language`: Your desired language. Only one language can be specified in a given `<voice>` tag. Specify your language in BCP-47 format. You can find the BCP-47 code for your language in the **language code** column on the [supported voices and languages page](https://docs.cloud.google.com/text-to-speech/docs/voices).



You can also control the relative priority of each of the `gender`, `variant`, and `language` attributes using two additional tags: `required` and `ordering`.

  * `required`: If an attribute is designated as `required` and not configured properly, the request will fail.
  * `ordering`: Any attributes listed after an `ordering` tag are considered as preferred attributes rather than required. The Cloud Text-to-Speech API considers preferred attributes on a best effort basis in the order they are listed after the `ordering` tag. If any preferred attributes are configured incorrectly, Cloud TTS might still return a valid voice but with the incorrect configuration dropped.



Examples of configurations using the `required` and `ordering` tags:
    
    
    <speak>And there it was <voice language="en-GB" gender="male" required="gender"
    ordering="gender language">a flying bird </voice>roaring in the skies for the
    first time.</speak>
    
    
    <speak>Today is supposed to be <voice language="en-GB" gender="female"
    ordering="language gender">Sunday Funday.</voice></speak>

## `<lang>`

You can use `<lang>` to include text in multiple languages within the same SSML request. All languages will be synthesized in the same voice unless you use the `<voice>` tag to explicitly change the voice. The `xml:lang` string must contain the target language in BCP-47 format (this value is listed as "language code" in the [supported voices](https://docs.cloud.google.com/text-to-speech/docs/voices) table). In the following example "chat" will be verbalized in French instead of the default language (English):

`<speak>The french word for cat is <lang xml:lang="fr-FR">chat</lang></speak>`

Cloud Text-to-Speech supports the `<lang>` tag on a best effort basis. Not all language combinations produce the same quality results if specified in same SSML request. In some cases, a language combination might produce an effect that is detectible but subtle or perceived as negative. Known issues:

  * Japanese with Kanji characters is not supported by the `<lang>` tag. The input is transliterated and read as Chinese characters.
  * Semitic languages such as Arabic, Hebrew, and Persian are not supported by the `<lang>` tag and will result in silence. If you want to use any of these languages we recommend using the `<voice>` tag to switch to a voice that speaks your desired language (if available).



## SSML timepoints

The Text-to-Speech API supports the use of timepoints in your created audio data. A **timepoint** is a timestamp (in seconds, measured from the beginning of the generated audio) that corresponds to a designated point in the script. You can set a timepoint in your script using the `<mark>` tag. When the audio is generated, the API then returns the time offset between the beginning of the audio and the timepoint.

There are two steps to setting a timepoint:

  1. Add a `<mark>` SSML tag to the point in the script that you want a timestamp for.
  2. Set [TimepointType](https://docs.cloud.google.com/text-to-speech/docs/reference/rest/v1beta1/text/synthesize#TimepointType) to `SSML_MARK`. If this field is not set, timepoints are not returned by default.



The following example returns two timepoints:

  * timepoint_1: Indicates the time (in seconds) that the word "Mark" appears in the generated audio.
  * timepoint_2: Indicates the time (in seconds) that the word "see" appears in the generated audio.


    
    
    <speak>Hello <mark name="timepoint_1"/> Mark. Good to <mark
    name="timepoint_2"/> see you.</speak>

## Styles

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The following voices can speak in multiple styles: 

  1. en-US-Neural2-F
  2. en-US-Neural2-J



Use the `<google:style>` tag to control what style to use. Only use the tag around full sentences. 

Example:
    
    
    <speak><google:style name="lively">Hello I'm so happy today!</google:style></speak>

The `name` field supports the following values:

  1. `apologetic`
  2. `calm`
  3. `empathetic`
  4. `firm`
  5. `lively`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
    * [ Builders Hub ](https://me.developers.google.com/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


