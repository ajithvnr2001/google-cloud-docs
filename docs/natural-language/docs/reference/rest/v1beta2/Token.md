---
url: https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token/
title: Token \u00a0|\u00a0 Cloud Natural Language API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:54:50.244731+00:00
---

# Token  |  Cloud Natural Language API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Natural Language API ](https://docs.cloud.google.com/natural-language/docs)
  * [ Reference ](https://docs.cloud.google.com/natural-language/docs/apis)



Send feedback 

#  Token Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * PartOfSpeech
    * JSON representation
  * Tag
  * Aspect
  * Case
  * Form
  * Gender
  * Mood
  * Number
  * Person
  * Proper
  * Reciprocity
  * Tense
  * Voice
  * DependencyEdge
    * JSON representation
  * Label



Represents the smallest syntactic building block of the text.

JSON representation  
---  
      
    
    {
      "text": {
        object ([TextSpan](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/TextSpan))
      },
      "partOfSpeech": {
        object ([PartOfSpeech](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#PartOfSpeech))
      },
      "dependencyEdge": {
        object ([DependencyEdge](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#DependencyEdge))
      },
      "lemma": string
    }  
  
Fields  
---  
`text` |  `object (`[TextSpan](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/TextSpan)`)` The token text.  
`partOfSpeech` |  `object (`[PartOfSpeech](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#PartOfSpeech)`)` Parts of speech tag for this token.  
`dependencyEdge` |  `object (`[DependencyEdge](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#DependencyEdge)`)` Dependency tree parse for this token.  
`lemma` |  `string` [Lemma](https://en.wikipedia.org/wiki/Lemma_%28morphology%29) of the token.  
  
## PartOfSpeech

Represents part of speech information for a token.

JSON representation  
---  
      
    
    {
      "tag": enum ([Tag](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Tag)),
      "aspect": enum ([Aspect](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Aspect)),
      "case": enum ([Case](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Case)),
      "form": enum ([Form](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Form)),
      "gender": enum ([Gender](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Gender)),
      "mood": enum ([Mood](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Mood)),
      "number": enum ([Number](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Number)),
      "person": enum ([Person](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Person)),
      "proper": enum ([Proper](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Proper)),
      "reciprocity": enum ([Reciprocity](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Reciprocity)),
      "tense": enum ([Tense](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Tense)),
      "voice": enum ([Voice](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Voice))
    }  
  
Fields  
---  
`tag` |  `enum (`[Tag](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Tag)`)` The part of speech tag.  
`aspect` |  `enum (`[Aspect](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Aspect)`)` The grammatical aspect.  
`case` |  `enum (`[Case](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Case)`)` The grammatical case.  
`form` |  `enum (`[Form](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Form)`)` The grammatical form.  
`gender` |  `enum (`[Gender](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Gender)`)` The grammatical gender.  
`mood` |  `enum (`[Mood](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Mood)`)` The grammatical mood.  
`number` |  `enum (`[Number](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Number)`)` The grammatical number.  
`person` |  `enum (`[Person](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Person)`)` The grammatical person.  
`proper` |  `enum (`[Proper](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Proper)`)` The grammatical properness.  
`reciprocity` |  `enum (`[Reciprocity](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Reciprocity)`)` The grammatical reciprocity.  
`tense` |  `enum (`[Tense](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Tense)`)` The grammatical tense.  
`voice` |  `enum (`[Voice](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Voice)`)` The grammatical voice.  
  
## Tag

The part of speech tags enum.

Enums  
---  
`UNKNOWN` | Unknown  
`ADJ` | Adjective  
`ADP` | Adposition (preposition and postposition)  
`ADV` | Adverb  
`CONJ` | Conjunction  
`DET` | Determiner  
`NOUN` | Noun (common and proper)  
`NUM` | Cardinal number  
`PRON` | Pronoun  
`PRT` | Particle or other function word  
`PUNCT` | Punctuation  
`VERB` | Verb (all tenses and modes)  
`X` | Other: foreign words, typos, abbreviations  
`AFFIX` | Affix  
  
## Aspect

The characteristic of a verb that expresses time flow during an event.

Enums  
---  
`ASPECT_UNKNOWN` | Aspect is not applicable in the analyzed language or is not predicted.  
`PERFECTIVE` | Perfective  
`IMPERFECTIVE` | Imperfective  
`PROGRESSIVE` | Progressive  
  
## Case

The grammatical function performed by a noun or pronoun in a phrase, clause, or sentence. In some languages, other parts of speech, such as adjective and determiner, take case inflection in agreement with the noun.

Enums  
---  
`CASE_UNKNOWN` | Case is not applicable in the analyzed language or is not predicted.  
`ACCUSATIVE` | Accusative  
`ADVERBIAL` | Adverbial  
`COMPLEMENTIVE` | Complementive  
`DATIVE` | Dative  
`GENITIVE` | Genitive  
`INSTRUMENTAL` | Instrumental  
`LOCATIVE` | Locative  
`NOMINATIVE` | Nominative  
`OBLIQUE` | Oblique  
`PARTITIVE` | Partitive  
`PREPOSITIONAL` | Prepositional  
`REFLEXIVE_CASE` | Reflexive  
`RELATIVE_CASE` | Relative  
`VOCATIVE` | Vocative  
  
## Form

Depending on the language, Form can be categorizing different forms of verbs, adjectives, adverbs, etc. For example, categorizing inflected endings of verbs and adjectives or distinguishing between short and long forms of adjectives and participles

Enums  
---  
`FORM_UNKNOWN` | Form is not applicable in the analyzed language or is not predicted.  
`ADNOMIAL` | Adnomial  
`AUXILIARY` | Auxiliary  
`COMPLEMENTIZER` | Complementizer  
`FINAL_ENDING` | Final ending  
`GERUND` | Gerund  
`REALIS` | Realis  
`IRREALIS` | Irrealis  
`SHORT` | Short form  
`LONG` | Long form  
`ORDER` | Order form  
`SPECIFIC` | Specific form  
  
## Gender

Gender classes of nouns reflected in the behaviour of associated words.

Enums  
---  
`GENDER_UNKNOWN` | Gender is not applicable in the analyzed language or is not predicted.  
`FEMININE` | Feminine  
`MASCULINE` | Masculine  
`NEUTER` | Neuter  
  
## Mood

The grammatical feature of verbs, used for showing modality and attitude.

Enums  
---  
`MOOD_UNKNOWN` | Mood is not applicable in the analyzed language or is not predicted.  
`CONDITIONAL_MOOD` | Conditional  
`IMPERATIVE` | Imperative  
`INDICATIVE` | Indicative  
`INTERROGATIVE` | Interrogative  
`JUSSIVE` | Jussive  
`SUBJUNCTIVE` | Subjunctive  
  
## Number

Count distinctions.

Enums  
---  
`NUMBER_UNKNOWN` | Number is not applicable in the analyzed language or is not predicted.  
`SINGULAR` | Singular  
`PLURAL` | Plural  
`DUAL` | Dual  
  
## Person

The distinction between the speaker, second person, third person, etc.

Enums  
---  
`PERSON_UNKNOWN` | Person is not applicable in the analyzed language or is not predicted.  
`FIRST` | First  
`SECOND` | Second  
`THIRD` | Third  
`REFLEXIVE_PERSON` | Reflexive  
  
## Proper

This category shows if the token is part of a proper name.

Enums  
---  
`PROPER_UNKNOWN` | Proper is not applicable in the analyzed language or is not predicted.  
`PROPER` | Proper  
`NOT_PROPER` | Not proper  
  
## Reciprocity

Reciprocal features of a pronoun.

Enums  
---  
`RECIPROCITY_UNKNOWN` | Reciprocity is not applicable in the analyzed language or is not predicted.  
`RECIPROCAL` | Reciprocal  
`NON_RECIPROCAL` | Non-reciprocal  
  
## Tense

Time reference.

Enums  
---  
`TENSE_UNKNOWN` | Tense is not applicable in the analyzed language or is not predicted.  
`CONDITIONAL_TENSE` | Conditional  
`FUTURE` | Future  
`PAST` | Past  
`PRESENT` | Present  
`IMPERFECT` | Imperfect  
`PLUPERFECT` | Pluperfect  
  
## Voice

The relationship between the action that a verb expresses and the participants identified by its arguments.

Enums  
---  
`VOICE_UNKNOWN` | Voice is not applicable in the analyzed language or is not predicted.  
`ACTIVE` | Active  
`CAUSATIVE` | Causative  
`PASSIVE` | Passive  
  
## DependencyEdge

Represents dependency parse tree information for a token.

JSON representation  
---  
      
    
    {
      "headTokenIndex": integer,
      "label": enum ([Label](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Label))
    }  
  
Fields  
---  
`headTokenIndex` |  `integer` Represents the head of this token in the dependency tree. This is the index of the token which has an arc going to this token. The index is the position of the token in the array of tokens returned by the API method. If this token is a root token, then the `headTokenIndex` is its own index.  
`label` |  `enum (`[Label](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1beta2/Token#Label)`)` The parse label for the token.  
  
## Label

The parse label enum for the token.

Enums  
---  
`UNKNOWN` | Unknown  
`ABBREV` | Abbreviation modifier  
`ACOMP` | Adjectival complement  
`ADVCL` | Adverbial clause modifier  
`ADVMOD` | Adverbial modifier  
`AMOD` | Adjectival modifier of an NP  
`APPOS` | Appositional modifier of an NP  
`ATTR` | Attribute dependent of a copular verb  
`AUX` | Auxiliary (non-main) verb  
`AUXPASS` | Passive auxiliary  
`CC` | Coordinating conjunction  
`CCOMP` | Clausal complement of a verb or adjective  
`CONJ` | Conjunct  
`CSUBJ` | Clausal subject  
`CSUBJPASS` | Clausal passive subject  
`DEP` | Dependency (unable to determine)  
`DET` | Determiner  
`DISCOURSE` | Discourse  
`DOBJ` | Direct object  
`EXPL` | Expletive  
`GOESWITH` | Goes with (part of a word in a text not well edited)  
`IOBJ` | Indirect object  
`MARK` | Marker (word introducing a subordinate clause)  
`MWE` | Multi-word expression  
`MWV` | Multi-word verbal expression  
`NEG` | Negation modifier  
`NN` | Noun compound modifier  
`NPADVMOD` | Noun phrase used as an adverbial modifier  
`NSUBJ` | Nominal subject  
`NSUBJPASS` | Passive nominal subject  
`NUM` | Numeric modifier of a noun  
`NUMBER` | Element of compound number  
`P` | Punctuation mark  
`PARATAXIS` | Parataxis relation  
`PARTMOD` | Participial modifier  
`PCOMP` | The complement of a preposition is a clause  
`POBJ` | Object of a preposition  
`POSS` | Possession modifier  
`POSTNEG` | Postverbal negative particle  
`PRECOMP` | Predicate complement  
`PRECONJ` | Preconjunt  
`PREDET` | Predeterminer  
`PREF` | Prefix  
`PREP` | Prepositional modifier  
`PRONL` | The relationship between a verb and verbal morpheme  
`PRT` | Particle  
`PS` | Associative or possessive marker  
`QUANTMOD` | Quantifier phrase modifier  
`RCMOD` | Relative clause modifier  
`RCMODREL` | Complementizer in relative clause  
`RDROP` | Ellipsis without a preceding predicate  
`REF` | Referent  
`REMNANT` | Remnant  
`REPARANDUM` | Reparandum  
`ROOT` | Root  
`SNUM` | Suffix specifying a unit of number  
`SUFF` | Suffix  
`TMOD` | Temporal modifier  
`TOPIC` | Topic marker  
`VMOD` | Clause headed by an infinite form of the verb that modifies a noun  
`VOCATIVE` | Vocative  
`XCOMP` | Open clausal complement  
`SUFFIX` | Name suffix  
`TITLE` | Name title  
`ADVPHMOD` | Adverbial phrase modifier  
`AUXCAUS` | Causative auxiliary  
`AUXVV` | Helper auxiliary  
`DTMOD` | Rentaishi (Prenominal modifier)  
`FOREIGN` | Foreign words  
`KW` | Keyword  
`LIST` | List for chains of comparable items  
`NOMC` | Nominalized clause  
`NOMCSUBJ` | Nominalized clausal subject  
`NOMCSUBJPASS` | Nominalized clausal passive  
`NUMC` | Compound of numeric modifier  
`COP` | Copula  
`DISLOCATED` | Dislocated relation (for fronted/topicalized elements)  
`ASP` | Aspect marker  
`GMOD` | Genitive modifier  
`GOBJ` | Genitive object  
`INFMOD` | Infinitival modifier  
`MES` | Measure  
`NCOMP` | Nominal complement of a noun  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-13 UTC."],[],[]] 
