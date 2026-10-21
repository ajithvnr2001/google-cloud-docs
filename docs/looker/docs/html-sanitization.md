---
url: https://docs.cloud.google.com/looker/docs/html-sanitization/
title: HTML sanitization \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:50:53.033601+00:00
---

# HTML sanitization  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/html-sanitization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  HTML sanitization Stay organized with collections  Save and categorize content based on your preferences. 

To prevent certain security exploits, Looker restricts which HTML tags, HTML tag attributes, and CSS properties are allowed in the [`html` parameter](https://docs.cloud.google.com/looker/docs/reference/param-field-html), in [custom welcome emails](https://docs.cloud.google.com/looker/docs/admin-panel-users-custom-welcome-email), and in [text tiles](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_tiles_and_text_to_a_dashboard) and [tile notes](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#adding_a_tile_note) in dashboards.

Looker strips any HTML elements that aren't supported from the rendered HTML. For example, the following HTML has unsupported HTML tags:
    
    
    <div class="pretty"><badtag></badtag></div>
    

Looker will render this as:
    
    
    <div class="pretty"></div>
    

As another example, the following HTML has unsupported HTML attributes:
    
    
    <div class="pretty" badattr="uh-oh"></div>
    

Looker will render this as:
    
    
    <div class="pretty"></div>
    

HTML sanitization is on by default and can't be edited.

## Allowed HTML tags

Only certain HTML tags will be rendered in the browser. Any other tags will be stripped from rendered HTML.

Here is the list of HTML tags that Looker supports:

` a `

` abbr `

` acronym `

` address `

` area `

` article `

` aside `

` audio `

` b `

` bdi `

` bdo `

` big `

` blockquote `

` br `

` button `

` canvas `

` caption `

` center `

` cite `

` code `

` col `

` colgroup `

` datalist `

` dd `

` del `

` details `

` dfn `

` dir `

` div `

` dl `

` dt `

` em `

` fieldset `

` figcaption `

` footer `

` h1 `

` h2 `

` h3 `

` h4 `

` h5 `

` h6 `

` header `

` ins `

` hr `

` i `

` img `

` kbd `

` label `

` legend `

` li `

` map `

` mark `

` menu `

` meter `

` nav `

` ol `

` output `

` p `

` pre `

` progress `

` q `

` s `

` samp `

` section `

` small `

` source `

` span `

` strike `

` strong `

` sub `

` summary `

` sup `

` table `

` tbody `

` td `

` tfoot `

` th `

` thead `

` time `

` tr `

` track `

` tt `

` u `

` ul `

` var `

` video `

## Allowed HTML tag attributes

Only certain HTML attributes will be rendered in the browser. Any other attributes will be stripped from rendered HTML. This also applies to the CSS properties for HTML `style` tags.

Here is the list of HTML attributes that Looker supports:

` abbr `

` accept `

` accept-charset `

` accesskey `

` action `

` align `

` alt `

` autoplay `

` axis `

` border `

` cellpadding `

` cellspacing `

` char `

` charoff `

` charset `

` checked `

` cite `

` class `

` clear `

` color `

` cols `

` colspan `

` compact `

` controls `

` controlslist `

` coords `

` datetime `

` dir `

` disabled `

` enctype `

` for `

` frame `

` headers `

` height `

` href `

` hreflang `

` hspace `

` id `

` ismap `

` label `

` lang `

` longdesc `

` loop `

` loopcount `

` loopend `

` loopstart `

` maxlength `

` media `

` method `

` multiple `

` muted `

` name `

` nohref `

` noshade `

` nowrap `

` poster `

` preload `

` prompt `

` readonly `

` rel `

` rev `

` rows `

` rowspan `

` rules `

` scope `

` selected `

` shape `

` size `

` span `

` src `

` start `

` style `

` summary `

` tabindex `

` target `

` title `

` type `

` usemap `

` valign `

` value `

` vspace `

` width `

` xml:lang `

## Allowed CSS Properties for HTML `style` Tags

Here is the list of allowed CSS properties that Looker supports:

` -moz-border-radius `

` -moz-border-radius-bottomleft `

` -moz-border-radius-bottomright `

` -moz-border-radius-topleft `

` -moz-border-radius-topright `

` -moz-box-shadow `

` -moz-outline `

` -moz-outline-color `

` -moz-outline-style `

` -moz-outline-width `

` -o-text-overflow `

` -webkit-border-bottom-left-radius `

` -webkit-border-bottom-right-radius `

` -webkit-border-radius `

` -webkit-border-radius-bottom-left `

` -webkit-border-radius-bottom-right `

` -webkit-border-radius-top-left `

` -webkit-border-radius-top-right `

` -webkit-border-top-left-radius `

` -webkit-border-top-right-radius `

` -webkit-box-shadow `

` azimuth `

` background `

` background-attachment `

` background-color `

` background-image` (note that `url` is unsupported) 

` background-position `

` background-repeat `

` border `

` border-bottom `

` border-bottom-color `

` border-bottom-left-radius `

` border-bottom-right-radius `

` border-bottom-style `

` border-bottom-width `

` border-collapse `

` border-color `

` border-left `

` border-left-color `

` border-left-style `

` border-left-width `

` border-radius `

` border-right `

` border-right-color `

` border-right-style `

` border-right-width `

` border-spacing `

` border-style `

` border-top `

` border-top-color `

` border-top-left-radius `

` border-top-right-radius `

` border-top-style `

` border-top-width `

` border-width `

` box-shadow `

` caption-side `

` clear `

` color `

` cue `

` cue-after `

` cue-before `

` cursor `

` direction `

` display `

` elevation `

` empty-cells `

` float `

` font `

` font-family `

` font-size `

` font-stretch `

` font-style `

` font-variant `

` font-weight `

` height `

` image() `

` letter-spacing `

` line-height `

` linear-gradient() `

` list-style `

` list-style-image `

` list-style-position `

` list-style-type `

` margin `

` margin-bottom `

` margin-left `

` margin-right `

` margin-top `

` max-height `

` max-width `

` min-height `

` min-width `

` outline `

` outline-color `

` outline-style `

` outline-width `

` overflow `

` padding `

` padding-bottom `

` padding-left `

` padding-right `

` padding-top `

` pause `

` pause-after `

` pause-before `

` pitch `

` pitch-range `

` quotes `

` radial-gradient() `

` rect() `

` repeating-linear-gradient() `

` repeating-radial-gradient() `

` rgb() `

` rgba() `

` richness `

` speak `

` speak-header `

` speak-numeral `

` speak-punctuation `

` speech-rate `

` stress `

` table-layout `

` text-align `

` text-decoration `

` text-indent `

` text-overflow `

` text-shadow `

` text-transform `

` text-wrap `

` unicode-bidi `

` vertical-align `

` voice-family `

` volume `

` white-space `

` width `

` word-spacing `

` word-wrap `

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-18 UTC."],[],[]] 
