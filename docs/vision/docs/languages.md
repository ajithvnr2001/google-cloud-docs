---
url: https://docs.cloud.google.com/vision/docs/languages/
title: OCR language support \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:24:49.588315+00:00
---

# OCR language support  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/languages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Reference ](https://docs.cloud.google.com/vision/docs/apis)



Send feedback 

#  OCR language support Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Vision's text recognition feature can detect many languages, including multiple languages in a single image. If the Vision API is having trouble automatically detecting a language, you can provide a language hint to help improve detection output.

To use these features and specify languages, see the guides for [detecting text](https://docs.cloud.google.com/vision/docs/ocr#specify-language) or [detecting handwriting](https://docs.cloud.google.com/vision/docs/handwriting#specify-the-language-optional). To try text detection with a language hint directly in your browser, see the [Try it](https://docs.cloud.google.com/vision/docs/ocr#try-it) section of the text detection pages.

### Specify language hints

You specify optional language hints in a request's [ImageContext](https://docs.cloud.google.com/vision/docs/reference/rest/v1/images/annotate#imagecontext) as a list of `languageHints` for a `TEXT_DETECTION` or `DOCUMENT_TEXT_DETECTION` request.

Each language code parameter consists of a [BCP-47](https://tools.ietf.org/html/bcp47) identifier. This parameter uses the form _language_ -_region_ , where:

  * _language_ : The primary language.
  * _region_ : An optional region, typically a country identifier, for a specific dialect.



For example, Chinese can be represented as Simplified Chinese, as written in the People's Republic of China (`zh-Hans`), or Traditional Chinese, as written in Taiwan (`zh-Hant`).

The text recognition feature supports three levels of language:

  1. **Supported** languages are those that Google prioritizes and regularly evaluates for performance.
  2. **Experimental** languages are those under active development but not regularly evaluated for performance.
  3. **Mapped** languages are supported by mapping to another language code or a general character recognizer. For example, `en-GB` is treated like `en` for text recognition. While Google attempts to return the correct mapped language code in the **Entity locale** field, these languages are more prone to misidentification as similar languages compared to fully supported or experimental ones.



If you leave the language hint blank, the service attempts to auto-detect the most appropriate language. Specifically:

  * The `TEXT_DETECTION` endpoint auto-detects only a subset of supported languages.
  * The `DOCUMENT_TEXT_DETECTION` endpoint auto-detects the full set of supported languages.



The list of languages (with associated `languageHint` codes) supported by `TEXT_DETECTION` and `DOCUMENT_TEXT_DETECTION` appears in the following list.

## Supported languages

The following languages are prioritized and regularly evaluated.

To filter the list of languages, type a language name in the search box:

Language | Language (English name) | `languageHints` code | Script | Notes  
---|---|---|---|---  
Afrikaans | Afrikaans | `af` | `Latn` | |   
shqip | Albanian | `sq` | `Latn` | |   
العربية | Arabic | `ar` | `Arab` | Modern Standard|   
Հայ | Armenian | `hy` | `Armn` | |   
беларуская | Belarusian | `be` | `Cyrl` | |   
বাংলা | Bengali | `bn` | `Beng` | |   
български | Bulgarian | `bg` | `Cyrl` | |   
Català | Catalan | `ca` | `Latn` | |   
普通话 | Chinese | `zh` | `Hans/Hant` | |   
Hrvatski | Croatian | `hr` | `Latn` | |   
Čeština | Czech | `cs` | `Latn` | |   
Dansk | Danish | `da` | `Latn` | |   
Nederlands | Dutch | `nl` | `Latn` | |   
English | English | `en` | `Latn` | American|   
Eesti keel | Estonian | `et` | `Latn` | |   
Filipino | Filipino | `fil` | `Latn` | |   
Suomi | Finnish | `fi` | `Latn` | |   
Français | French | `fr` | `Latn` | European|   
Deutsch | German | `de` | `Latn` | |   
Ελληνικά | Greek | `el` | `Grek` | |   
ગુજરાતી | Gujarati | `gu` | `Gujr` | |   
עברית | Hebrew | `iw` | `Hebr` | |   
हिन्दी | Hindi | `hi` | `Deva` | |   
Magyar | Hungarian | `hu` | `Latn` | |   
Íslenska | Icelandic | `is` | `Latn` | |   
Bahasa Indonesia | Indonesian | `id` | `Latn` | |   
Italiano | Italian | `it` | `Latn` | |   
日本語 | Japanese | `ja` | `Jpan` | |   
ಕನ್ನಡ | Kannada | `kn` | `Knda` | |   
ភាសាខ្មែរ | Khmer | `km` | `Khmr` | |   
한국어 | Korean | `ko` | `Kore` | |   
ລາວ | Lao | `lo` | `Laoo` | |   
Latviešu | Latvian | `lv` | `Latn` | |   
Lietuvių | Lithuanian | `lt` | `Latn` | |   
Македонски | Macedonian | `mk` | `Cyrl` | |   
Bahasa Melayu | Malay | `ms` | `Latn` | |   
മലയാളം | Malayalam | `ml` | `Mlym` | |   
मराठी | Marathi | `mr` | `Deva` | |   
नेपाली | Nepali | `ne` | `Deva` | |   
Norsk | Norwegian | `no` | `Latn` | Bokmål|   
فارسی | Persian | `fa` | `Arab` | |   
Polski | Polish | `pl` | `Latn` | |   
Português | Portuguese | `pt` | `Latn` | Brazilian|   
ਪੰਜਾਬੀ | Punjabi | `pa` | `Guru` | Gurmukhi|   
Română | Romanian | `ro` | `Latn` | |   
Русский | Russian | `ru` | `Cyrl` | |   
Русский (старая орфография) | Russian | `ru-PETR1708` | `Cyrl` | Old Orthography|   
Српски | Serbian | `sr` | `Cyrl` | |   
Српски (латиница) | Serbian | `sr-Latn` | `Latn` | |   
Slovenčina | Slovak | `sk` | `Latn` | |   
Slovenščina | Slovenian | `sl` | `Latn` | |   
Español | Spanish | `es` | `Latn` | European|   
Svenska | Swedish | `sv` | `Latn` | |   
Tagalog | Tagalog | `tl` | `Latn` | |   
தமிழ் | Tamil | `ta` | `Taml` | |   
తెలుగు | Telugu | `te` | `Telu` | |   
ไทย | Thai | `th` | `Thai` | |   
Türkçe | Turkish | `tr` | `Latn` | |   
Українська | Ukrainian | `uk` | `Cyrl` | |   
Tiếng Việt | Vietnamese | `vi` | `Latn` | |   
Yiddish | Yiddish | `yi` | `Hebr` | |   
  
## Experimental languages

The following languages are under active development and not yet regularly evaluated against.

Language | Language (English name) | `languageHints` code | Script | Notes  
---|---|---|---|---  
አማርኛ | Amharic | `am` | `Ethi` | |   
Αρχαία ελληνικά | Ancient Greek | `grc` | `Grek` | |   
অসমীয়া | Assamese | `as` | `Beng` | |   
Azərbaycan | Azerbaijani | `az` | `Latn` | |   
Azərbaycan (qədim yazı) | Azerbaijani | `az-Cyrl` | `Cyrl` | Old Orthography|   
Euskara | Basque | `eu` | `Latn` | |   
Bosanski | Bosnian | `bs` | `Latn` | |   
မြန်မာ | Burmese | `my` | `Mymr` | |   
Cebuano | Cebuano | `ceb` | `Latn` | |   
ᏣᎳᎩ ᎦᏬᏂᎯᏍᏗ | Cherokee | `chr` | `Cher` | |   
dhivehi, dhivehi-bas | Dhivehi | `dv` | `Thaa` | |   
རྫོང་ཁ | Dzonkha | `dz` | `Tibt` | |   
Esperanto | Esperanto | `eo` | `Latn` | |   
Galego | Galician | `gl` | `Latn` | |   
ქართული | Georgian | `ka` | `Geor` | |   
Kreyòl Ayisyen | Haitian Creole | `ht` | `Latn` | |   
Gaeilge | Irish | `ga` | `Latn` | |   
Jawa | Javanese | `jv` | `Latn` | |   
Қазақ | Kazakh | `kk` | `Cyrl` | |   
Kirghiz | Kirghiz | `ky` | `Cyrl` | |   
Latine | Latin | `la` | `Latn` | |   
Malti | Maltese | `mt` | `Latn` | |   
Монгол | Mongolian | `mn` | `Cyrl` | |   
ଓଡ଼ିଆ | Oriya | `or` | `Orya` | |   
پښتو | Pashto | `ps` | `Arab` | |   
संस्कृतम् | Sanskrit | `sa` | `Deva` | |   
සිංහල | Sinhala | `si` | `Sinh` | |   
Swahili | Swahili | `sw` | `Latn` | |   
leššānā Suryāyā | Syriac | `syr` | `Syriac` | |   
བོད་སྐད་ | Tibetan | `bo` | `Tibt` | |   
ትግርኛ | Tigirinya | `ti` | `Ethi` | |   
اردو | Urdu | `ur` | `Arab` | |   
oʻzbekcha | Uzbek | `uz` | `Latn` | Latin|   
oʻzbekcha | Uzbek | `uz-Cyrl` | `Cyrl` | Old Orthography|   
Cymraeg | Welsh | `cy` | `Latn` | |   
IsiZulu | Zulu | `zu` | `Latn` | |   
  
## Mapped languages

The following languages are mapped to another language code or mapped to a general character recognizer.

Language | Language (English name) | `languageHints` code | Script | Notes  
---|---|---|---|---  
بهسا اچيه | Acehnese | `ace` | `Latn` | Latin model|   
Lwo | Acholi | `ach` | `Latn` | Latin model|   
Dangme | Adangme | `ada` | `Latn` | Latin model|   
Akan | Akan | `ak` | `Latn` | Latin model|   
Anicinâbemowin | Algonquinian | `alg` | `Latn` | Latin model|   
Mapudungu | Araucanian/Mapuche | `arn` | `Latn` | Latin model|   
Asturianu | Asturian | `ast` | `Latn` | Latin model|   
Dene | Athabaskan | `ath` | `Latn` | Latin model|   
Aymar aru | Aymara | `ay` | `Latn` | Latin model|   
Bhāṣa Bali | Balinese | `ban` | `Latn` | Latin model|   
Bamanankan | Bambara | `bm` | `Latn` | Latin model|   
Narrow Bantu | Bantu | `bnt` | `Latn` | Latin model|   
башҡорт теле | Bashkir | `ba` | `Cyrl` | Cyrillic model|   
Toba–Batak | Batak | `btk` | `Latn` | Latin model|   
Chibemba | Bemba | `bem` | `Latn` | Latin model|   
Bikol Naga | Bikol | `bik` | `Latn` | Latin model|   
Bichelamar | Bislama | `bi` | `Latn` | Latin model|   
Brezhoneg | Breton | `br` | `Latn` | Latin model|   
нохчийн мотт / noxçiyn mott | Chechen | `ce` | `Cyrl` | Cyrillic model|   
汉语 | Chinese (Mandarin, Simplified,) | `zh-Hans` | `Hans` | Chinese model|   
漢語 | Chinese (Mandarin, Traditional) | `zh-Hant` | `Hant` | Chinese model|   
普通話 | Chinese (Mandarin, Hong Kong) | `zh-Hant-HK` | `Hant` | Chinese model|   
Chahta' | Choctaw | `cho` | `Latn` | Latin model|   
Чӑвашла | Chuvash | `cv` | `Cyrl` | Cyrillic model|   
Cree–Montagnais–Naskapi | Cree | `cr` | `Latn` | Latin model|   
Mvskoke | Creek | `mus` | `Latn` | Latin model|   
qırımtatar tili, къырымтатар тили | Crimean Tatar | `crh` | `Latn` | Cyrillic model|   
Dakhótiyapi, Dakȟótiyapi | Dakota | `dak` | `Latn` | Latin model|   
Douala | Duala | `dua` | `Latn` | Latin model|   
Ikɔ Efik | Efik | `efi` | `Latn` | Latin model|   
English (British) | English (British) | `en-GB` | `Latn` | Latin model|   
Èʋegbe | Ewe | `ee` | `Latn` | Latin model|   
føroyskt mál | Faroese | `fo` | `Latn` | Latin model|   
Na Vosa Vakaviti | Fijian | `fj` | `Latn` | Latin model|   
fɔ̀ngbè | Fon | `fon` | `Latn` | Latin model|   
Français canadien | French (Canadian) | `fr-CA` | `Latn` | Latin model|   
Fulani, Fulah, Peul | Fulah | `ff` | `Latn` | Latin model|   
Gã | Ga | `gaa` | `Latn` | Latin model|   
Luganda | Ganda | `lg` | `Latn` | Latin model|   
Basa Gayo | Gayo | `gay` | `Latn` | Latin model|   
Kiribati | Gilbertese | `gil` | `Latn` | Latin model|   
Gothic | Gothic | `got` | `Latn` | Latin model|   
Guaraní | Guarani | `gn` | `Latn` | Latin model|   
Harshen/Halshen Hausa هَرْشَن هَوْسَ | Hausa | `ha` | `Latn` | Latin model|   
ʻŌlelo Hawaiʻi | Hawaiian | `haw` | `Latn` | Latin model|   
Otjiherero | Herero | `hz` | `Latn` | Latin model|   
Ilonggo | Hiligaynon | `hil` | `Latn` | Latin model|   
Jaku Iban | Iban | `iba` | `Latn` | Latin model|   
Asụsụ Igbo | Igbo | `ig` | `Latn` | Latin model|   
Ilokano | Iloko | `ilo` | `Latn` | Latin model|   
Taqbaylit | Kabyle | `kab` | `Latn` | Latin model|   
Jingpho | Kachin | `kac` | `Latn` | Latin model|   
Kalaallisut | Kalaallisut | `kl` | `Latn` | Latin model|   
Kikamba | Kamba | `kam` | `Latn` | Latin model|   
Kanuri | Kanuri | `kr` | `Latn` | Latin model|   
Qaraqalpaq tili, Қарақалпақ тили, قاراقالپاق تىلى | Kara-Kalpak | `kaa` | `Cyrl/Latn` | Cyrillic model|   
Ka Ktien Khasi | Khasi | `kha` | `Latn` | Latin model|   
Gĩkũyũ | Kikuyu | `ki` | `Latn` | Latin model|   
Kinyarwanda | Kinyarwanda | `rw` | `Latn` | Latin model|   
коми кыв | Komi | `kv` | `Cyrl` | Cyrillic model|   
Kikongo | Kongo | `kg` | `Latn` | Latin model|   
Kosraean | Kosraean | `kos` | `Latn` | Latin model|   
Oshikwanyama | Kuanyama | `kj` | `Latn` | Latin model|   
Ngala | Lingala | `ln` | `Latn` | Latin model|   
Plattdütsch, Plattdeutsch, Nedersaksisch | Low German | `nds` | `Latn` | Latin model|   
siLozi | Lozi | `loz` | `Latn` | Latin model|   
Kiluba | Luba-Katanga | `lu` | `Latn` | Latin model|   
Dholuo | Luo | `luo` | `Latn` | Latin model|   
Madhura, Basa Mathura, بَهاسَ مَدورا | Madurese | `mad` | `Latn` | Latin model|   
Malagasy | Malagasy | `mg` | `Latn` | Latin model|   
Mandinka, لغة مندنكا | Mandingo | `man` | `Latn` | Latin model|   
Gaelg, Gailck | Manx | `gv` | `Latn` | Latin model|   
Te reo Māori | Maori | `mi` | `Latn` | Latin model|   
Ebon | Marshallese | `mh` | `Latn` | Latin model|   
Mɛnde yia | Mende | `men` | `Latn` | Latin model|   
Middle English | Middle English | `enm` | `Latn` | Latin model|   
Mittelhochdeutsch | Middle High German | `gmh` | `Latn` | Latin model|   
Baso Minangkabau, باسو مينڠكاباو | Minangkabau | `min` | `Latn` | Latin model|   
Kanienʼkéha | Mohawk | `moh` | `Latn` | Latin model|   
Nkundu | Mongo | `lol` | `Latn` | Latin model|   
Nāhuatl | Nahuatl | `nah` | `Latn` | Latin model|   
Diné bizaad | Navajo | `nv` | `Latn` | Latin model|   
Ndonga | Ndonga | `ng` | `Latn` | Latin model|   
ko e vagahau Niuē | Niuean | `niu` | `Latn` | Latin model|   
Zimbabwe Ndebele | North Ndebele | `nd` | `Latn` | Latin model|   
Sesotho sa Leboa | Northern Sotho | `nso` | `Latn` | Latin model|   
Chichewa, Chinyanja | Nyanja | `ny` | `Latn` | Latin model|   
Runyankore | Nyankole | `nyn` | `Latn` | Latin model|   
Chitonga | Nyasa Tonga | `tog` | `Latn` | Latin model|   
Appolo | Nzima | `nzi` | `Latn` | Latin model|   
Occitan, lenga d'òc, provençal | Occitan | `oc` | `Latn` | Latin model|   
Anishinaabemowin, ᐊᓂᔑᓈᐯᒧᐎᓐ | Ojibwa | `oj` | `Latn` | Latin model|   
Ænglisc, Englisc, Anglisc | Old English | `ang` | `Latn` | Latin model|   
Franceis, François, Romanz | Old French | `fro` | `Latn` | Latin model|   
Diutisk, Althochdeutsch | Old High German | `goh` | `Latn` | Latin model|   
Dǫnsk tunga | Old Norse | `non` | `Latn` | Latin model|   
Occitan ancian | Old Provencal | `pro` | `Latn` | Latin model|   
ирон ӕвзаг | Ossetic | `os` | `Cyrl` | Cyrillic model|   
Kapampangan | Pampanga | `pam` | `Latn` | Latin model|   
Salitan Pangasinan | Pangasinan | `pag` | `Latn` | Latin model|   
Papiamentu | Papiamento | `pap` | `Latn` | Latin model|   
Português (Portugal) | Portuguese (European) | `pt-PT` | `Latn` | Latin model|   
Kechua / Runa Simi | Quechua | `qu` | `Latn` | Latin model|   
Rumantsch | Romansh | `rm` | `Latn` | Latin model|   
Romani čhib | Romany | `rom` | `Latn` | Latin model|   
Ikirundi | Rundi | `rn` | `Latn` | Latin model|   
Sakha | Sakha | `sah` | `Cyrl` | Cyrillic model|   
Gagana faʻa Sāmoa | Samoan | `sm` | `Latn` | Latin model|   
yângâ tî sängö | Sango | `sg` | `Latn` | Latin model|   
(Braid) Scots, Lallans, Doric | Scots | `sco` | `Latn` | Latin model|   
Gàidhlig | Scottish Gaelic | `gd` | `Latn` | Latin model|   
chiShona | Shona | `sn` | `Latn` | Latin model|   
Songhay | Songhai | `son` | `Latn` | Latin model|   
Sesotho | Southern Sotho | `st` | `Latn` | Latin model|   
Español (Latinoamérica) | Spanish (Latin American) | `es-419` | `Latn` | Latin model|   
ᮘᮞ ᮞᮥᮔ᮪ᮓ , Basa Sunda | Sundanese | `su` | `Latn` | Latin model|   
siSwati | Swati | `ss` | `Latn` | Latin model|   
Reo Tahiti | Tahitian | `ty` | `Latn` | Latin model|   
тоҷикӣ | Tajik | `tg` | `Cyrl` | Cyrillic model|   
татар теле | Tatar | `tt` | `Cyrl/Latn` | Cyrillic model|   
KʌThemnɛ | Temne | `tem` | `Latn` | Latin model|   
lea faka-Tonga | Tongan | `to` | `Latn` | Latin model|   
Xitsonga | Tsonga | `ts` | `Latn` | Latin model|   
Setswana | Tswana | `tn` | `Latn` | Latin model|   
Türkmençe | Turkmen | `tk` | `Latn` | Cyrillic model|   
удмурт кыл | Udmurt | `udm` | `Cyrl` | Cyrillic model|   
Tshivenḓa | Venda | `ve` | `Latn` | Latin model|   
Vod | Votic | `vot` | `Cyrl/Latn` | Cyrillic model|   
Frysk | Western Frisian | `fy` | `Latn` | Latin model|   
Wolof | Wolof | `wo` | `Latn` | Latin model|   
isiXhosa | Xhosa | `xh` | `Latn` | Latin model|   
Èdè Yorùbá | Yoruba | `yo` | `Latn` | Latin model|   
Diidxazá | Zapotec | `zap` | `Latn` | Latin model|   
  
### Handwriting scripts

The following scripts are supported for handwriting recognition. See the language tables for languages that use each script.

Script | Name | Support Level  
---|---|---  
`Beng` | Bengali | Experimental  
`Cyrl` | Cyrillic | Experimental  
`Deva` | Devanagari | Experimental  
`Grek` | Greek | Experimental  
`Hani` | Chinese | Experimental  
`Jpan` | Japanese | Supported  
`Kore` | Korean | Supported  
`Latn` | Latin | Supported  
`vi` | Vietnamese | Experimental  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
