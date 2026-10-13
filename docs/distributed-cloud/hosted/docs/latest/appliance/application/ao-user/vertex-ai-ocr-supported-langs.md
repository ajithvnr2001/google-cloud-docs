---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-ocr-supported-langs/
title: Supported languages \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:14.021535+00:00
---

# Supported languages  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-ocr-supported-langs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Supported languages Stay organized with collections  Save and categorize content based on your preferences. 

The text recognition feature of Google Distributed Cloud (GDC) air-gapped appliance detects a variety of languages and can detect multiple languages in a single image.

You can specify an optional language hint to an Optical Character Recognition (OCR) API request. For example, you might want to provide a hint when the API is having trouble detecting the language used in your image.

To specify optional language hints, add them to your `BatchAnnotateImages` or `BatchAnnotateFiles` request in the `image_context` field as a list of values in the `language_hints` field.

The `language_hints` format uses the following `BCP 47` language tag formatting guidelines:
    
    
    language["-" script] ["-" region] *("-" variant) *("-" extension) ["-" privateuse]
    

For example, the language hint `en-t-i0-handwrit` indicates that the language is "English transformed from handwriting."

The text recognition feature supports three levels of language:

  1. _Supported_ languages are prioritized with regular performance evaluation.
  2. _Experimental_ languages are under active development. They don't have regular performance evaluations.
  3. _Mapped_ languages are supported by mapping them to another language code or a general character recognizer. For example, `en-GB` is supported but not treated differently than `en` for text recognition. The OCR service tries to return the correct mapped language code in the `entity` field. However, mapped languages are more likely to be misidentified than fully or experimentally supported languages.



One of the key features of the OCR service is the capability to [detect and extract text from images](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/quickstart-ocr-images). An image can be, for example, handwritten text. For a list of handwriting scripts that are supported for handwriting recognition, see Handwriting scripts.

## Supported languages

The text recognition feature prioritizes and regularly evaluates supported languages. To filter by language, type a language in the following field:

Language | Language (English name) | Language hints code | Script and notes  
---|---|---|---  
Afrikaans | Afrikaans | `af` | Latn  
shqip | Albanian | `sq` | Latn  
العربية | Arabic | `ar` | Arab; Modern Standard  
беларуская | Belarusian | `be` | Cyrl  
български | Bulgarian | `bg` | Cyrl  
Català | Catalan | `ca` | Latn  
普通话 | Chinese | `zh` | Hans/Hant  
Hrvatski | Croatian | `hr` | Latn  
Čeština | Czech | `cs` | Latn  
Dansk | Danish | `da` | Latn  
Nederlands | Dutch | `nl` | Latn  
English | English  | `en` | Latn; American  
Eesti keel | Estonian | `et` | Latn  
Filipino | Filipino | `fil` or `tl` | Latn  
Suomi | Finnish | `fi` | Latn  
Français | French  | `fr` | Latn; European  
Deutsch | German | `de` | Latn  
Ελληνικά | Greek | `el` | Grek  
עברית | Hebrew | `iw` | Hebr  
हिन्दी | Hindi | `hi` | Deva  
Magyar | Hungarian | `hu` | Latn  
Íslenska | Icelandic | `is` | Latn  
Bahasa Indonesia | Indonesian | `id` | Latn  
Italiano | Italian | `it` | Latn  
日本語 | Japanese | `ja` | Jpan  
한국어 | Korean | `ko` | Kore  
Latviešu | Latvian | `lv` | Latn  
Lietuvių | Lithuanian | `lt` | Latn  
Македонски | Macedonian | `mk` | Cyrl  
Bahasa Melayu | Malay | `ms` | Latn  
മലയാളം | Malayalam | `ml` | Mlym  
मराठी | Marathi | `mr` | Deva  
नेपाली | Nepali | `ne` | Deva  
Norsk | Norwegian | `no` | Latn; Bokmål  
فارسی | Persian | `fa` | Arab  
Polski | Polish | `pl` | Latn  
Português | Portuguese | `pt` | Latn; Brazilian  
Română | Romanian | `ro` | Latn  
Русский | Russian | `ru` | Cyrl  
Русский (старая орфография) | Russian | `ru-PETR1708` | Cyrl; Old Orthography  
Српски | Serbian | `sr` | Cyrl & Latn  
Српски (латиница) | Serbian | `sr-Latn` | Latn  
Slovenčina | Slovak | `sk` | Latn  
Slovenščina | Slovenian | `sl` | Latn  
Español | Spanish | `es` | Latn; European  
Svenska | Swedish | `sv` | Latn  
Tagalog | Tagalog | `tl` | Latn  
Türkçe | Turkish | `tr` | Latn  
Українська | Ukrainian | `uk` | Cyrl  
Tiếng Việt | Vietnamese | `vi` | Latn  
Yiddish | Yiddish | `yi` | Hebr  
  
## Experimental languages

Experimental languages are under active development and not evaluated. To filter by language, type a language in the following field:

Language | Language (English name) | Language hints code | Script and notes  
---|---|---|---  
Αρχαία ελληνικά | Ancient Greek | `grc` | Grek  
Azərbaycan | Azerbaijani | `az` | Latn  
Azərbaycan (qədim yazı) | Azerbaijani | `az-Cyrl` | Cyrl; old orthography  
Euskara | Basque | `eu` | Latn  
Bosanski | Bosnian | `bs` | Latn  
Cebuano | Cebuano | `ceb` | Latn  
Esperanto | Esperanto | `eo` | Latn  
Galego | Galician | `gl` | Latn  
ქართული | Georgian | `ka` | Geor  
Kreyòl Ayisyen | Haitian Creole | `ht` | Latn  
Gaeilge | Irish | `ga` | Latn  
Jawa | Javanese | `jv` | Latn  
Қазақ | Kazakh | `kk` | Cyrl  
Kirghiz | Kirghiz | `ky` | Cyrl  
Latine | Latin | `la` | Latn  
Malti | Maltese | `mt` | Latn  
Монгол | Mongolian | `mn` | Cyrl  
پښتو | Pashto | `ps` | Arab  
संस्कृतम् | Sanskrit | `sa` | Deva  
Swahili | Swahili | `sw` | Latn  
اردو | Urdu | `ur` | Arab  
oʻzbekcha | Uzbek | `uz` | Latn; Latin  
oʻzbekcha | Uzbek | `uz-Cyrl` | Cyrl; old orthography  
Cymraeg | Welsh | `cy` | Latn  
IsiZulu | Zulu | `zu` | Latn  
  
## Mapped languages

Mapped languages are associated with another language code or a general character recognizer. To filter by language, type a language in the following field:

Language | Language (English name) | Language hints code | Script and notes | Mapped to  
---|---|---|---|---  
بهسا اچيه | Acehnese | `ace` | Latn | Latin script model  
Lwo | Acholi | `ach` | Latn | Latin script model  
Dangme | Adangme | `ada` | Latn | Latin script model  
Akan | Akan | `ak` | Latn | Latin script model  
Anicinâbemowin | Algonquinian | `alg` | Latn | Latin script model  
Mapudungu | Araucanian/Mapuche | `arn` | Latn | Latin script model  
Asturianu | Asturian | `ast` | Latn | Latin script model  
Dene | Athabaskan | `ath` | Latn | Latin script model  
Aymar aru | Aymara | `ay` | Latn | Latin script model  
Bhāṣa Bali | Balinese | `ban` | Latn | Latin script model  
Bamanankan | Bambara | `bm` | Latn | Latin script model  
Narrow Bantu | Bantu | `bnt` | Latn | Latin script model  
башҡорт теле | Bashkir | `ba` | Cyrl | Cyrillic script model  
Toba–Batak | Batak | `btk` | Latn | Latin script model  
Chibemba | Bemba | `bem` | Latn | Latin script model  
Bikol Naga | Bikol | `bik` | Latn | Latin script model  
Bichelamar | Bislama | `bi` | Latn | Latin script model  
Brezhoneg | Breton | `br` | Latn | Latin script model  
нохчийн мотт / noxçiyn mott | Chechen | `ce` | Cyrl | Cyrillic script model  
汉语 | Chinese | `zh-Hans` | Hans; Simplified; Mandarin | zh  
漢語 | Chinese | `zh-Hant` | Hant; Traditional; Mandarin | zh  
普通話 | Chinese | `zh-Hant-HK` | Hant; Mandarin; Hong Kong | zh  
Chahta' | Choctaw | `cho` | Latn | Latin script model  
Чӑвашла | Chuvash | `cv` | Cyrl | Cyrillic script model  
Cree–Montagnais–Naskapi | Cree | `cr` | Latn | Latin script model  
Mvskoke | Creek | `mus` | Latn | Latin script model  
qırımtatar tili, къырымтатар тили | Crimean Tatar | `crh` | Latn | Cyrillic script model  
Dakhótiyapi, Dakȟótiyapi | Dakota | `dak` | Latn | Latin script model  
Douala | Duala | `dua` | Latn | Latin script model  
Ikɔ Efik | Efik | `efi` | Latn | Latin script model  
English (British) | English  | `en-GB` | Latn; British | en  
Èʋegbe | Ewe | `ee` | Latn | Latin script model  
føroyskt mál | Faroese | `fo` | Latn | Latin script model  
Na Vosa Vakaviti | Fijian | `fj` | Latn | Latin script model  
fɔ̀ngbè | Fon | `fon` | Latn | Latin script model  
Français canadien | French | `fr-CA` | Latn; Canadian | fr  
Fulani, Fulah, Peul | Fulah | `ff` | Latn | Latin script model  
Gã | Ga | `gaa` | Latn | Latin script model  
Luganda | Ganda | `lg` | Latn | Latin script model  
Basa Gayo | Gayo | `gay` | Latn | Latin script model  
Kiribati | Gilbertese | `gil` | Latn | Latin script model  
Gothic | Gothic | `got` | Latn | Latin script model  
Guaraní | Guarani | `gn` | Latn | Latin script model  
Harshen/Halshen Hausa هَرْشَن هَوْسَ | Hausa | `ha` | Latn | Latin script model  
ʻŌlelo Hawaiʻi | Hawaiian | `haw` | Latn | Latin script model  
Otjiherero | Herero | `hz` | Latn | Latin script model  
Ilonggo | Hiligaynon | `hil` | Latn | Latin script model  
Jaku Iban | Iban | `iba` | Latn | Latin script model  
Asụsụ Igbo | Igbo | `ig` | Latn | Latin script model  
Ilokano | Iloko | `ilo` | Latn | Latin script model  
Taqbaylit | Kabyle | `kab` | Latn | Latin script model  
Jingpho | Kachin | `kac` | Latn | Latin script model  
Kalaallisut | Kalaallisut | `kl` | Latn | Latin script model  
Kikamba | Kamba | `kam` | Latn | Latin script model  
Kanuri | Kanuri | `kr` | Latn | Latin script model  
Qaraqalpaq tili, Қарақалпақ тили, قاراقالپاق تىلى | Kara-Kalpak | `kaa` | Cyrl/Latn | Cyrillic script model  
Ka Ktien Khasi | Khasi | `kha` | Latn | Latin script model  
Gĩkũyũ | Kikuyu | `ki` | Latn | Latin script model  
Kinyarwanda | Kinyarwanda | `rw` | Latn | Latin script model  
коми кыв | Komi | `kv` | Cyrl | Cyrillic script model  
Kikongo | Kongo | `kg` | Latn | Latin script model  
Kosraean | Kosraean | `kos` | Latn | Latin script model  
Oshikwanyama | Kuanyama | `kj` | Latn | Latin script model  
Ngala | Lingala | `ln` | Latn | Latin script model  
Plattdütsch, Plattdeutsch, Nedersaksisch | Low German | `nds` | Latn | Latin script model  
siLozi | Lozi | `loz` | Latn | Latin script model  
Kiluba | Luba-Katanga | `lu` | Latn | Latin script model  
Dholuo | Luo | `luo` | Latn | Latin script model  
Madhura, Basa Mathura, بَهاسَ مَدورا | Madurese | `mad` | Latn | Latin script model  
Malagasy | Malagasy | `mg` | Latn | Latin script model  
Mandinka, لغة مندنكا | Mandingo | `man` | Latn | Latin script model  
Gaelg, Gailck | Manx | `gv` | Latn | Latin script model  
Te reo Māori | Maori | `mi` | Latn | Latin script model  
Ebon | Marshallese | `mh` | Latn | Latin script model  
Mɛnde yia  | Mende | `men` | Latn | Latin script model  
Middle English | Middle English | `enm` | Latn | Latin script model  
Mittelhochdeutsch | Middle High German | `gmh` | Latn | Latin script model  
Baso Minangkabau, باسو مينڠكاباو | Minangkabau | `min` | Latn | Latin script model  
Kanienʼkéha | Mohawk | `moh` | Latn | Latin script model  
Nkundu | Mongo | `lol` | Latn | Latin script model  
Nāhuatl | Nahuatl | `nah` | Latn | Latin script model  
Diné bizaad | Navajo | `nv` | Latn | Latin script model  
Ndonga | Ndonga | `ng` | Latn | Latin script model  
ko e vagahau Niuē | Niuean | `niu` | Latn | Latin script model  
Zimbabwe Ndebele | North Ndebele | `nd` | Latn | Latin script model  
Sesotho sa Leboa | Northern Sotho | `nso` | Latn | Latin script model  
Chichewa, Chinyanja | Nyanja | `ny` | Latn | Latin script model  
Runyankore | Nyankole | `nyn` | Latn | Latin script model  
Chitonga | Nyasa Tonga | `tog` | Latn | Latin script model  
Appolo | Nzima | `nzi` | Latn | Latin script model  
Occitan, lenga d'òc, provençal | Occitan | `oc` | Latn | Latin script model  
Anishinaabemowin, ᐊᓂᔑᓈᐯᒧᐎᓐ | Ojibwa | `oj` | Latn | Latin script model  
Ænglisc, Englisc, Anglisc | Old English | `ang` | Latn | Latin script model  
Franceis, François, Romanz | Old French | `fro` | Latn | Latin script model  
Diutisk, Althochdeutsch | Old High German | `goh` | Latn | Latin script model  
Dǫnsk tunga | Old Norse | `non` | Latn | Latin script model  
Occitan ancian | Old Provencal | `pro` | Latn | Latin script model  
ирон ӕвзаг | Ossetic | `os` | Cyrl | Cyrillic script model  
Kapampangan | Pampanga | `pam` | Latn | Latin script model  
Salitan Pangasinan | Pangasinan | `pag` | Latn | Latin script model  
Papiamentu | Papiamento | `pap` | Latn | Latin script model  
Português (Portugal) | Portuguese | `pt-PT` | Latn; European | pt  
Kechua / Runa Simi | Quechua | `qu` | Latn | Latin script model  
Rumantsch | Romansh | `rm` | Latn | Latin script model  
Romani čhib | Romany | `rom` | Latn | Latin script model  
Ikirundi | Rundi | `rn` | Latn | Latin script model  
Sakha | Sakha | `sah` | Cyrl | Cyrillic script model  
Gagana faʻa Sāmoa | Samoan | `sm` | Latn | Latin script model  
yângâ tî sängö | Sango | `sg` | Latn | Latin script model  
(Braid) Scots, Lallans, Doric | Scots | `sco` | Latn | Latin script model  
Gàidhlig | Scottish Gaelic | `gd` | Latn | Latin script model  
chiShona | Shona | `sn` | Latn | Latin script model  
Songhay | Songhai | `son` | Latn | Latin script model  
Sesotho | Southern Sotho | `st` | Latn | Latin script model  
Español (Latinoamérica) | Spanish | `es-419` | Latn; Latin American | es  
ᮘᮞ ᮞᮥᮔ᮪ᮓ , Basa Sunda | Sundanese | `su` | Latn | Latin script model  
siSwati | Swati | `ss` | Latn | Latin script model  
Reo Tahiti | Tahitian | `ty` | Latn | Latin script model  
тоҷикӣ | Tajik | `tg` | Cyrl | Cyrillic script model  
татар теле | Tatar | `tt` | Cyrl/Latn | Cyrillic script model  
KʌThemnɛ | Temne | `tem` | Latn | Latin script model  
lea faka-Tonga | Tongan | `to` | Latn | Latin script model  
Xitsonga | Tsonga | `ts` | Latn | Latin script model  
Setswana | Tswana | `tn` | Latn | Latin script model  
Türkmençe | Turkmen | `tk` | Latn | Cyrillic script model  
удмурт кыл | Udmurt | `udm` | Cyrl | Cyrillic script model  
Tshivenḓa | Venda | `ve` | Latn | Latin script model  
Vod | Votic | `vot` | Cyrl/Latn | Cyrillic script model  
Frysk | Western Frisian | `fy` | Latn | Latin script model  
Wolof | Wolof | `wo` | Latn | Latin script model  
isiXhosa | Xhosa | `xh` | Latn | Latin script model  
Èdè Yorùbá | Yoruba | `yo` | Latn | Latin script model  
Diidxazá | Zapotec | `zap` | Latn | Latin script model  
  
## Handwriting scripts

This section contains the scripts that are supported for handwriting recognition. To learn which languages use each script, refer to the tables for supported, experimental, and mapped languages. To filter by script, type a script in the following field:

Script tag | Name | Support level  
---|---|---  
Beng | Bengali | Experimental  
Cyrl | Cyrillic | Experimental  
Deva | Devanagari | Experimental  
Grek | Greek | Experimental  
Hani | Chinese | Experimental  
Jpan | Japanese | Supported  
Kore | Korean | Supported  
Latn | Latin | Supported  
vi | Vietnamese | Experimental  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-08 UTC."],[],[]] 
