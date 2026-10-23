---
url: https://docs.cloud.google.com/natural-language/docs/morphology/
title: Morphology & Dependency Trees \u00a0|\u00a0 Cloud Natural Language API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:36.740362+00:00
---

# Morphology & Dependency Trees  |  Cloud Natural Language API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/natural-language/docs/morphology/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Natural Language API ](https://docs.cloud.google.com/natural-language/docs)
  * [ Guides ](https://docs.cloud.google.com/natural-language/docs/setup)



Send feedback 

#  Morphology & Dependency Trees Stay organized with collections  Save and categorize content based on your preferences. 

The `analyzeSyntax` method returns details about the linguistic structure of the given text. For each [token](https://docs.cloud.google.com/natural-language/reference/rest/v1/Token) in the text, the Natural Language API provides information about its internal structure (morphology) and its role in the sentence (syntax).

[Morphology](https://en.wikipedia.org/wiki/Morphology_\(linguistics\)) is the study of the internal structure of words.. Morphology focuses on how the components within a word (stems, root words, prefixes, suffixes, etc.) are arranged or modified to create different meanings. English, for example, often adds "-s" or "-es" to the end of count nouns to indicate plurality, and a "-d" or "-ed" to a verb to indicate past tense. The suffix “-ly” is added to adjectives to create adverbs (for example, “happy” [adjective] and “happily” [adverb]).

The Natural Language API uses morphological analysis to infer grammatical information about words.

Morphology varies greatly between languages. In languages such as Russian, word endings indicate the role of a word in a sentence (for example, “книга” [book - nominative case] becomes “книгу” [accusative case] when it’s the direct object of a verb). This means word order can vary without changing the meaning of the sentence, though different word order does impact contextual appropriateness. Languages such as English and Mandarin, which both lack affixes indicating case, rely more on the word order in a sentence to indicate the respective roles of words. As a result, morphological analysis depends heavily on the source language, and an understanding of what is supported within that language.

[Syntax](https://en.wikipedia.org/wiki/Syntax) is the study of the structure of phrases and sentences. Syntax and morphology work together to indicate grammatical relationships, with different languages dividing the labor between them differently. For example, Russian uses an affix to indicate the role of direct object (“у” in “книгу”), whereas English uses word order, where the direct object follows the verb (read the book).

The `analyzeSyntax` response returns morphological information in the `partOfSpeech` field and the syntactic relationship between words in the `dependencyTree` field.

## Parts of Speech

Within a syntactic request, part-of-speech and morphological information are returned within the response's `partOfSpeech` field. The `partOfSpeech` field contains a set of sub-fields with Part-of-Speech (POS) information as well as more explicit morphological information. These subfields are listed below.

  * `tag` denotes the part of speech using a coarse-grained POS tag (NOUN, VERB, etc.), and provides top-level surface syntax information. POS tags are helpful if you want to create patterns and/or reduce ambiguity for subsequent language analysis (for example, “train” tagged as a NOUN versus a VERB).

  * `number` denotes a word's [grammatical number](https://en.wikipedia.org/wiki/Grammatical_number). In English, the suffix "-s" is added to [count nouns](https://en.wikipedia.org/wiki/Count_noun) to indicate more than one (for example, “dog+s” indicates more than one dog). Absence of the plural suffix is often referred to as the singular form. Some languages, such as Arabic, have the notion of a [dual number](https://en.wikipedia.org/wiki/Dual_\(grammatical_number\)) as well. This field may contain the following values:

    * `SINGULAR` denotes one quantity.
    * `PLURAL` denotes more than one quantity.
    * `DUAL` denotes precisely two quantities.
  * `person` identifies a word's [grammatical person](https://en.wikipedia.org/wiki/Grammatical_person). In English, “I/me” is 1st person singular and references the speaker (or writer) of the expression, whereas “you” and “she/her and he/him” reference the intended addressee (hearer) and some other person, respectively. This field may contain the following values:

    * `FIRST` person denotes the speaker.
    * `SECOND` person denotes intended addressee, that is, the person spoken to.
    * `THIRD` person denotes non-speaker/non-hearer.
    * `REFLEXIVE_PERSON` indicates, for example, the subject and the object reference the same entity, as in “The cat licked itself,” where -self attaches to a pronoun to indicate reflexivity. In Russian and Japanese, the reflexive is a standalone pronoun. (for example, “John loves himself” in Russian is “Джон любит себя” where себя is gender neutral “self”; in Japanese it’s “Tarō wa zibun o aisuru” (Romanized version) where “zibun” is gender neutral “self.” See [reflexive pronoun](https://en.wikipedia.org/wiki/Reflexive_pronoun).
  * `gender` denotes a noun's [grammatical gender](https://en.wikipedia.org/wiki/Grammatical_gender). This field may contain the following values:

    * The `FEMININE` grammatical gender
    * The `MASCULINE` grammatical gender
    * The `NEUTER` grammatical gender
  * `case` denotes a word's [grammatical case](https://en.wikipedia.org/wiki/Grammatical_case) and its [role](https://en.wikipedia.org/wiki/Grammatical_relation) in a phrase or sentence. This field may contain the following values::

    * The [`ACCUSATIVE` case](https://en.wikipedia.org/wiki/Accusative_case) indicates the direct object of a transitive verb.
    * The [`ADVERBIAL` case](https://en.wikipedia.org/wiki/Adverbial_case) indicates an adverbial form of an adjective. Note that English uses separate words adverbs ("well") and adjectives ("good"). The suffix -ly in English does derive adverbs from adjectives (for example, “happy,” “happily”), though it’s not considered a “case”.
    * The `COMPLEMENTIVE` case (Chinese) indicates a word necessary to complete the meaning of a potential, descriptive, or resultative expression using a conjunctive particle.
    * The [`DATIVE` case](https://en.wikipedia.org/wiki/Dative_case) indicates an indirect object, which refers to the referent receiving the direct object. In English, the indirect object is often indicated by the preposition "to" as in the phrase "He gave the ball to Bobby," where “Bobby” is the indirect object, and is the recipient of the ball. Whereas in this Russian example: Иван дал книгу маше (Ivan gave the book to Masha), “-e” indicates “маше” is the indirect object, and Masha is the recipient of the book.
    * The [`GENITIVE` case](https://en.wikipedia.org/wiki/Genitive_case) indicates possession. Note that English often indicates possession using the "-'s" affix instead of using a genitive case. The "-'s" affix can can attach to the end of a phrase (for example, “[The man who ran the bill up]’s wife paid a dear price for his excess.”). Whereas in this Russian example, “-а” marks “Антон-” as genitive: “Где книга Антона?” (Where is Anton’s book). In Russian, the genitive case also shows up as the complement of words like “several,” “few.” For example: Зимой здесь мало снега (“In winter there is little snow here”) “-a” marks “снег-” (snow) as genitive, since it is the complement of “мало” (“little”). There is no possession involved.
    * The [`INSTRUMENTAL` case](https://en.wikipedia.org/wiki/Instrumental_case) indicates whether a noun is the instrument by which an action is completed. In Russian, the English sentence, "He opened the door with a key," would be: “он открыл дверь ключом” where “-om” attaches to “ключ” (key) indicating instrumental case.
    * The [`LOCATIVE` case](https://en.wikipedia.org/wiki/Locative_case) indicates a word's use to refer to a location. English, does not have a locative case. 
    * The [`NOMINATIVE` case](https://en.wikipedia.org/wiki/Nominative_case) is associated with the subject of a verb. In English, the subject of a sentence is indicated through word order, not case. In the sentence, “The girl won the race,” the phrase “the girl” is the subject, appearing to the left of the verb, “won.” In Russian, девушка (the/a girl) can appear either before or after the verb: “девушка выиграла гонку” or “гонку выиграла девушка”, where the verb is выиграла (won).
    * The [`OBLIQUE` case](https://en.wikipedia.org/wiki/Oblique_case) indicates a word's use as an object to either a verb or preposition.
    * The [`PARTITIVE` case](https://en.wikipedia.org/wiki/Partitive) indicates a word's "partialness" or lack of specific identity. An example of a partitive in English would be “three of my friends.” In Russian, this would be “трое моих друзей” where “трое” is “three of” (compare with “три друга” where “три” is “three”).
    * The [`PREPOSITIONAL` case](https://en.wikipedia.org/wiki/Prepositional_case) indicates the object of a preposition.
    * The `REFLEXIVE_CASE` indicates the identity of an object of a verb to its subject. Most languages do not use a reflexive case, as this usage is indicated through use of special reflexive pronouns instead (such as "himself", "myself", etc.")
    * The `RELATIVE_CASE` (Chinese) indicates the complementizer of a relative clause connecting a noun with a verb or adjective. Examples: 工作 [的] 地方 (work [] place :: "place [where I] work"). 便宜 的 餐馆 (inexpensive [] restaurants :: restaurants [that are] inexpensive).
    * The [`VOCATIVE` case](https://en.wikipedia.org/wiki/Vocative_case) indicates a noun being used to address someone or something, usually when spoken to.
  * `tense` denotes a verb's [grammatical tense](https://en.wikipedia.org/wiki/Grammatical_tense), which indicates the verb's reference to a position in time. Note that `tense` is distinct from `aspect`, which also deals with a verb's relationship to time, but focuses on the characteristics of that time flow, rather than its position. The `IMPERFECT` and `PLUPERFECT` tenses in many languages more accurately refer to specific combinations of tense and aspect. This field may contain the following values:

    * `CONDITIONAL_TENSE` is an alternate term for the more prevalent morphological term of "conditional mood." (See `CONDITIONAL_MOOD` below.)
    * [`FUTURE`](https://en.wikipedia.org/wiki/Future_tense) denotes an action taking place in the future. Note that in English, the future tense is most often denoted by adding the word "will" to a verb phrase.
    * [`PAST`](https://en.wikipedia.org/wiki/Past_tense) denotes an action taking place in the past.
    * [`PRESENT`](https://en.wikipedia.org/wiki/Present_tense) denotes an action taking place in the present.
    * [`IMPERFECT`](https://en.wikipedia.org/wiki/Imperfect) denotes an action taking place in the past, but which was not completed at that tense's frame of reference. Note that in English, the imperfect tense is most often denoted by adding a gerund form of a verb to the past tense as in "I was walking." An imperfect tense event takes place in the past, but is not completed relative to that past tense.
    * [`PLUPERFECT`](https://en.wikipedia.org/wiki/Pluperfect) denotes an action that has taken place in the past, and was also completed at that tense's frame of reference. For example, "I had walked" takes place in the past, but was also complete during the past tense's frame of reference.
  * `aspect` denotes a verb's [grammatical aspect](https://en.wikipedia.org/wiki/Grammatical_aspect), its expression of time flow. Unlike `tense`, which focuses on a verb's position within time, `aspect` focuses on the characteristics of that time flow where it occurs. This field may contain the following values:

    * The [`PERFECTIVE` aspect](https://en.wikipedia.org/wiki/Perfective_aspect) denotes an event that is "completed" either because it has completely happened in the past or will completely happen in the future.
    * The [`IMPERFECTIVE` aspect](https://en.wikipedia.org/wiki/Imperfective_aspect) denotes an event that is incomplete, either because it is continuous or because it is repeated.
    * The [`PROGRESSIVE` aspect](https://en.wikipedia.org/wiki/Continuous_and_progressive_aspects) denotes an event that is continuous. A progressive aspect is generally treated as a special case of the more general imperfective aspect (which also covers repetition).



  * `mood` denotes a verb's [grammatical mood](https://en.wikipedia.org/wiki/Grammatical_mood), which indicates attitude about an underlying action. This field may contain the following values:

    * [`CONDITIONAL_MOOD`](https://en.wikipedia.org/wiki/Conditional_mood) indicates an action which is contingent. Note that in English, verb forms are not conditional; instead, conditional behavior is noted through use of the word "would" combined with the verb's infinitive.
    * [`IMPERATIVE`](https://en.wikipedia.org/wiki/Imperative_mood) indicates a command or request through the second person.
    * [`INDICATIVE`](https://en.wikipedia.org/wiki/Realis_mood) indicates a statement of fact, more generally known as a "realis mood."
    * [`INTERROGATIVE`](https://en.wikipedia.org/wiki/Interrogative) indicates a question.
    * [`JUSSIVE`](https://en.wikipedia.org/wiki/Jussive_mood) indicates a command or request through either the first or third person. English does not have a jussive mood, though exhortations that begin with a real or implied "Let us" convey this jussive mood.
    * [`SUBJUNCTIVE`](https://en.wikipedia.org/wiki/Subjunctive_mood) indicates a quality of uncertainty related to an action, also known as an "irrealis" mood (contrasted with the "realis" indicative mood). English does not have a specific subjunctive mood; instead, words such as "want", "wish", "hope", etc. convey the import of the subjunctive mood.
  * `voice` denotes a verb's [grammatical voice](https://en.wikipedia.org/wiki/Voice_\(grammar\)), the relationship between an action and a subject and/or object. This field may contain the following values:

    * [`ACTIVE` voice](https://en.wikipedia.org/wiki/Active_voice) indicates an action whose subject is performing the action.
    * [`CAUSATIVE` voice](https://en.wikipedia.org/wiki/Causative) indicates an action whose effect is being performed on the subject. In English, no direct causative voice exists; instead, such causation is indicated through use of the verb "make", as in "Mom made me go to school."
    * [`PASSIVE` voice](https://en.wikipedia.org/wiki/Passive_voice) indicates an action whose effect is being performed on the subject. In many cases, a passive "agent" is unspoken or unknown.
  * `reciprocity` denotes a word's (typically a pronoun's) [reciprocity](https://en.wikipedia.org/wiki/Reciprocal_pronoun), indicating the pronoun refers to a noun phrase elsewhere within the sentence. This field may contain the following values:

    * `RECIPROCAL` indicates the pronoun is reciprocal.
    * `NON_RECIPROCAL` indicates the pronoun is not reciprocal.
  * `proper` denotes whether a noun is part of a proper name. Note that many proper names consist of several words; if this phrase is detected as a proper name, each token will be detected as proper as well. (For example, both "Wrigley" and "Field" in the proper name "Wrigley Field" will have their proper attribute set to `PROPER`. This field may contain the following values:

    * `PROPER` denotes that the token is part of a proper name.
    * `NOT_PROPER` denotes that the token is not part of a proper name.
  * `form` denotes additional morphological forms that don't neatly fit into the previous set of common forms (`tense`,`mood`,`person`, etc.) Most of these forms are specific to unique languages. This field may contain the following values:

    * `ADNOMIAL` (Korean/Japanese) indicates a word ending (Korean) or verb (Japanese) that modifies a noun phrase. Examples: 밥을 먹는 사람 [someone who eats rice] and 書く人 [someone who writes].
    * `AUXILIARY` (Korean) indicates a word ending that connects two adjacent main and auxiliary predicates: 밥을 먹게 하다 [make (someone) to eat]
    * `COMPLEMENTIZER` (Korean) indicates a word ending that connects two or more different clauses: 밥을 먹고 물을 마신다 [ (I) eat rice and drink water]
    * `FINAL_ENDING` (Korean/Japanese) indicates a word ending that finalizes the clause or sentence coming at the end of the clause or sentence. Examples: 밥을 먹는다 [(I) eat rice] and 手紙を書く [write a letter].
    * `GERUND` (Korean/Japanese) indicates a word ending that nominalizes verbs or adjectives: (Korean) 밥 먹기 [eating rice] or connects verbs with various auxiliary verbs: (Japanese) 書きたい [want to write]
    * `REALIS` (Japanese) indicates conditional and subjunctive forms with a conjunctive particle “ば”: 書けば [if (I) write].
    * `IRREALIS` (Japanese) indicates connecting verbs with negative, passive, or causative auxiliary verbs: 書かない [do not write], 書かれる [to be written], 書かせる [make (someone) write].
    * `ORDER` (Japanese) indicates a command verb, similar to imperitive: 書け! [write!]
    * `SPECIFIC` (Japanese) indicates special forms that cannot be covered by the six categories above. The most common use of this form is a derivation of a noun from an adjective by adding a suffix to the form: かわいさ [cuteness]
    * `SHORT` (Russian) indicates a [short-form adjective or participle](https://en.wikibooks.org/wiki/Russian/Grammar/Adjectives#Short_adjectives).
    * `LONG` (Russian) indicates a long-form adjective or participle, as distinct from the above `SHORT` form.



Note that the Natural Language API provides morphological information on a per-token basis (not per phrase). Morphological constructs that cross word boundaries may not be supported.

## Dependency trees

Within a syntactic request, part-of-speech and morphological information are returned within the response's `partOfSpeech` field.

For each sentence within the text provided to the Natural Language API for syntactic analysis, the API constructs a _dependency tree_ that describes the syntactic structure of that sentence. The syntactic information are returned within the response's `dependencyEdge` field.

A diagram of the dependency tree for this single sentence from [John F. Kennedy's Inaugural speech](https://en.wikipedia.org/wiki/Inauguration_of_John_F._Kennedy) appears below:

![](https://docs.cloud.google.com/static/natural-language/docs/images/jfk-1961.png)

For each token, the `dependencyEdge` element identifies which other token it modifies (in the `headTokenIndex` field) and the syntactic relationship between this token and its head token (in the [`label`](https://docs.cloud.google.com/natural-language/reference/rest/v1/documents/annotateText#Label) field). For example, here is the `dependencyEdge` element for the token "your" in (the first occurrence of) the phrase "your country":
    
    
          "dependencyEdge": {
            "headTokenIndex": 4,
            "label": "POSS"
          },
    

This element indicates that "your" modifies the fifth token (`headTokenIndex` uses a zero-based offset) and that it is a possessive modifier.

Every dependency tree includes a `ROOT` element (`"label": ROOT`), which corresponds to the main verb in the sentence. In the above example, the `ROOT` element happens to be the first word in the sentence (`"headTokenIndex": 0`). For the `ROOT` word "Ask", the `headTokenIndex` is its own index.

Although parse trees do not cross sentence boundaries, the Natural Language API indexes sentences and tokens using zero-based offset values within the text as a whole.

The Natural Language API labels syntactic relationships using a common set of dependencies that apply across the [supported languages](https://docs.cloud.google.com/natural-language/docs/languages). The labels are described below. In example text, "Head" and the label appear below the tokens to which they apply.

Label | Description  
---|---  
`UNKNOWN` | Unknown relationship  
`ABBREV` | An abbreviation of the head token.  

    
    
    British Broadcasting Company (BBC)
                         Head     ABBREV
      
  
`ACOMP` | An adjectival phrase that functions as a complement (like an object of the verb). This relation specifically includes `be` copula constructions with adjective predicates. 
    
    
    The book looks heavy.
             Head  ACOMP
    
    The book is   heavy.
             Head ACOMP
    

The tag also applies to non-argument adjective adjuncts and in [raising constructions](https://en.wikipedia.org/wiki/Raising_\(linguistics\)) with adjectival predicates. 
    
    
    She arrived sad.
        Head    ACOMP
    
    I consider John intelligent.
      Head          ACOMP
      
  
`ADVCL` | An adverbial clause modifying a verb, such as a temporal clause, consequence, conditional clause, or purpose clause.  

    
    
    The accident happened as the night was falling.
                 Head                      ADVCL
    
    If you know who did it, you should tell the teacher.
           ADVCL                       Head
    
    He talked to him in order to secure the account.
       Head                      ADVCL
      
  
`ADVPHMOD` | Adverbial phrase modifier (Japanese)  
`ADVMOD` | A (non-clausal) adverb or adverbial phrase that serves to modify the meaning of a word.  

    
    
    Genetically modified food.
    ADVMOD      Head
    
    less   often
    ADVMOD Head
    
    About  200 people came to the party.
    ADVMOD Head
      
  
`AMOD` | An adjectival phrase that serves to modify the meaning of a noun phrase.  

    
    
    Sam eats red  meat.
             AMOD Head
    
    Sam took out a 3 million dollar loan.
                             AMOD   Head
      
  
`APPOS` | A noun phrase immediately to the right of another noun phrase, with the second phrase serving to define or modify the first.  

    
    
    Sam, my brother, arrived.
    Head    APPOS
    
    Bill (John’s cousin)
    Head         APPOS
      
  
`ATTR` | A nominal phrase headed by a copular verb. Note that ``ATTR`` is different from ``ACOMP`` in that the dependent is a noun phrase, not an adjective.  

    
    
    He is  a doctor.
       Head ATTR
    
    She resembles her mother.
        Head          ATTR
    

In questions, the wh-pronoun or the noun in the wh-phrase is in the ``ATTR`` relation to the ``ROOT``. 
    
    
    What is  your name?
    ATTR Head     NSUBJ
    
    What breed is   the dog?
         ATTR  Head     NSUBJ
    

[Raising constructions](https://en.wikipedia.org/wiki/Raising_\(linguistics\)) with nominal predicates also use the ``ATTR`` relation. 
    
    
    I consider John an intelligent person.
      Head                         ATTR
      
  
`AUX` | A non-main verb, such as a modal auxiliary or a form of ``be``, ``do``, or ``have`` in a periphrastic tense. Excludes the use of ``be`` as an auxiliary in a passive construction.  

    
    
    Reagan has died.
           AUX Head
    
    He should leave.
       AUX    Head
      
  
`AUXPASS` | A non-main verb of a clause in the passive voice.  

    
    
    Kennedy has been    killed.
            AUX AUXPASS Head
    
    Kennedy was/got killed.
            AUXPASS Head
      
  
`CC` | The relation between an element of a conjunct and the coordinating conjunction. One conjunct of a conjunction (normally the first) is treated as the head of the conjunction.  

    
    
    Bill is big  and honest.
            Head CC
    
    They either ski  or snowboard.
                Head CC
    
    Bill went to Florida but Jane traveled to Alaska.
         Head            CC
      
  
`CCOMP` | A dependent clause with an internal subject that functions like an object of the verb or adjective.  

    
    
    He says that you like  to swim.
       Head          CCOMP
    
    I am certain that he did   it.
         Head            CCOMP
    
    I admire the fact that you are   honest.
                 Head          CCOMP
      
  
`CONJ` | The relation between two elements connected by a coordinating conjunction, such as ``and`` or ``or``. The head of the relation is the first conjunct and other conjunctions depend on it via the ``conj`` relation.  

    
    
    Bill is big and honest.
            Head    CONJ
    
    They either ski  or snowboard.
                Head    CONJ
    
    We have apples, pears, oranges, and bananas.
            DOBJ    CONJ   CONJ         CONJ
      
  
`CSUBJ` | A clausal syntactic subject of a clause; that is, the subject is itself a clause ("What she said" in the example below).  

    
    
    What she said  makes sense.
             CSUBJ Head
      
  
`CSUBJPASS` | A clausal syntactic subject of a passive clause.  

    
    
    That she lied was suspected by everyone.
             CSUBJ    Head
      
  
`DEP` | The system is unable to determine a more precise dependency relation between two words.  

    
    
    Then, as if  to show that he could, . . .
             DEP    Head
    
    travel agency florence kentucky
           Head   DEP
      
  
`DET` | The relation between the head of a noun phrase and its determiner.  

    
    
    The man is here.
    DET Head
    
    Which book do you prefer?
    DET   Head
      
  
`DISCOURSE` | Interjections and other discourse elements that are not clearly linked to the structure of the sentence, except in an expressive way. Examples are interjections (``'oh'``, ``'uh-huh'``, ``'Welcome'``), fillers (``'um'``, ``'ah'``), and discourse markers (``'well'``, ``'like'``, ``'actually'``, but not ``'you know'``).  

    
    
    Iguazu is   in Argentina :)
           Head              DISCOURSE
      
  
`DOBJ` | The noun phrase that is the ([accusative](https://en.wikipedia.org/wiki/Accusative_case)) object of a verb.  

    
    
    She gave me a raise.
        Head      DOBJ
    
    They win  the lottery.
         Head     DOBJ
      
  
`EXPL` | Pleonastic nominal. In English, this is some uses of ``it`` and ``there``: the existential ``there``, and ``it`` when used in extraposition constructions. An expletive or pleonastic nominal is one where the nominal does not satisfy a semantic role of the predicate. In languages with expletives, they can be positioned in the subject and direct object slots.  

    
    
    There is   a ghost in the room.
    EXPL  Head   NSUBJ
    
    It   is clear that we should decline.
    EXPL Head
      
  
`GOESWITH` | Links two parts of a word that are separated in text.   
`IOBJ` | The noun phrase that is the ([dative](https://en.wikipedia.org/wiki/Dative_case)) indirect object of a verb.  

    
    
    She gave me   a present.
        Head IOBJ   DOBJ
      
  
`MARK` | The word introducing a finite or non-finite subordinate clause, such as ``'that'`` or ``'whether'``. The head is the head of the subordinate clause.  

    
    
    Forces engaged in fighting after insurgents attacked.
                               MARK             Head
    
    He says that you like to swim.
            MARK     Head
      
  
`MWE` | One of the two relations (alongside ``NN``) for compounding. It is used for certain fixed grammaticized expressions with function words that behave like a single function word. Multiword expressions are annotated in a flat, head-initial structure, in which all words in the expression modify the first one using the ``MWE`` label.  

    
    
    I like dogs as   well as  cats.
                Head MWE  MWE
    
    He cried because of  you.
             Head    MWE
      
  
`MWV` | Multi-word verbal expression.  
`NEG` | The relation between a negation word and the word it modifies.  

    
    
    Bill is    not a scientist.
         Head  NEG
    
    Bill is no  scientist.
            NEG Head
      
  
`NN` | Any noun that serves to modify the head noun.  

    
    
    phone book
    NN    Head
    
    oil price futures
    NN  NN    Head
      
  
`NPADVMOD` | A noun phrase used as an adverbial modifier.  

    
    
    The director is 65 years    old.
                       NPADVMOD Head
    
    Six feet     long
        NPADVMOD Head
    
    Shares eased a fraction.
           HEAD    NPADVMOD
    
    The silence is itself   significant.
                   NPADVMOD Head
    
    90% of Australians like him, the most     of any country.
                       Head          NPADVMOD
      
  
`NSUBJ` | A noun phrase that is the syntactic subject of a clause.  

    
    
    Clinton defeated Dole.
    NSUBJ   Head
    
    The baby  is   cute
        NSUBJ Head
      
  
`NSUBJPASS` | A noun phrase that is the syntactic subject of a passive clause.  

    
    
    Dole       was defeated by Clinton.
    NSUBJPASS      Head
      
  
`NUM` | Any number phrase that serves to modify the meaning of the noun with a quantity.  

    
    
    Sam ate three sheep.
            NUM   Head
      
  
`NUMBER` | Part of a number phrase.  

    
    
    I have four   thousand sheep.
           NUMBER Head
      
  
`P` | Any piece of punctuation in a clause.   
`PARATAXIS` | The parataxis relation (from Greek for “place side by side”) is a relation between a word (often the main predicate of a sentence) and other elements placed side by side without any explicit coordination, subordination, or argument relation with the head word. Parataxis is a discourse-like equivalent of coordination.  

    
    
    Let's face it we're annoyed.
    Head                PARATAXIS
    
    The guy, John said,     left early in the morning.
                  PARATAXIS Head
      
  
`PARTMOD` | Participial modifier  
`PCOMP` | Used when the complement of a preposition is a clause or prepositional phrase (or occasionally, an adverbial phrase).  

    
    
    We have no information on   whether users are   at risk.
                           Head               PCOMP
    
    They heard about you missing classes.
               Head      PCOMP
      
  
`POBJ` | The head of a noun phrase following a preposition or the adverbs ``'here'`` and ``'there'``.  

    
    
    I sat on   the chair.
          Head     POBJ
    
    What does CPR stand for?
    POBJ                Head
      
  
`POSS` | A possessive determiner or [genitive](https://en.wikipedia.org/wiki/Genitive_case) modifier.  

    
    
    their offices
    POSS  Head
    
    Bill’s clothes.
    POSS   Head
      
  
`POSTNEG` | Postverbal negative particle  
`PRECOMP` | Predicate complement  
`PRECONJ` | A word that appears at the beginning bracketing a conjunction, such as ``'either'``, ``'both'``, ``'neither'``).  

    
    
    Both    the boys and the girls are here.
    PRECONJ     Head
      
  
`PREDET` | A word that precedes and modifies the meaning of a noun phrase determiner.  

    
    
    All    the boys are here.
    PREDET     Head
      
  
`PREF` | Prefix  
`PREP` | Any prepositional phrase that serves to modify the meaning of a verb, adjective, noun, or even another preposition.  

    
    
    I saw a cat  in   a hat.
            Head PREP
    
    I saw  a cat with a telescope.
      Head       PREP
    
    He is responsible for  meals.
          Head        PREP
      
  
`PRONL` | The relationship between a verb and verbal morpheme (French)  
`PRT` | A verb particle.  

    
    
    They shut down the station.
         Head PRT
    
    He would not put  up  with it.
                 Head PRT
      
  
`PS` | Associative or possessive marker  
`QUANTMOD` | Quantifier phrase modifier  
`RCMOD` | A link from a noun to the verb which heads a relative clause.  

    
    
    I saw the man  you love.
              Head     RCMOD
    
    the book that you bought
        Head          RCMOD
    
    Bell, a company which is based in LA, makes and distributes computer products.
            Head             RCMOD
      
  
`RCMODREL` | Complementizer in relative clause (Chinese)  
`RDROP` | Ellipsis without a preceding predicate (Japanese)  
`REF` | Referent (Hindi)  
`REMNANT` | Used for ellipsis.  

    
    
    John won bronze, Mary silver, and Sandy gold.
             Head         REMNANT           REMNANT
      
  
`REPARANDUM` | Indicates disfluencies overridden in a speech repair.  

    
    
    Go to         the righ- to   the left.
       REPARANDUM           Head
      
  
`ROOT` | The root of the sentence. In vast majority of cases it is a verb.  
`SNUM` | Suffix specifying a unit of number(Japanese)  
`SUFF` | Suffix  
`TMOD` | A bare noun phrase constituent that serves to modify the meaning of the constituent by specifying a time. ``TMOD`` captures temporal points and duration; it does not capture repetition (``'two times'``, which would be an ``'NPADVMOD'``).  

    
    
    Last night, I swam in the pool.
         TMOD     Head
      
  
`TOPIC` | Topic marker (Chinese)  
`VMOD` | A clause headed by an infinite form of the verb.  

    
    
    Berries gathered on this side of the mountain are sweeter.
    Head    VMOD
    
    He sat  in the armchair reading the morning newspaper.
       Head                 VMOD
    
    I have nothing to say  to them.
           Head       VMOD
      
  
`VOCATIVE` | Marks a dialogue participant addressed in text (common in emails and newsgroup postings).  

    
    
    Anna,    can you bring a tent?
    VOCATIVE         Head
      
  
`XCOMP` | A clausal complement without its own subject, whose reference is determined by an external subject.  

    
    
    He says that you like to swim.
                     Head    XCOMP
    
    I am ready to leave.
         Head     XCOMP
      
  
`SUFFIX` | Name suffix  
`TITLE` | Name title  
`AUXCAUS` | Causative auxiliary (Japanese)  
`AUXVV` | Helper auxiliary (Japanese)  
`DTMOD` | Rentaishi (Prenominal modifier)  
`FOREIGN` | Foreign words  
`KW` | Keyword  
`LIST` | List for chains of comparable items  
`NOMC` | Nominalized clause  
`NOMCSUBJ` | Nominalized clausal subject  
`NOMCSUBJPASS` | Nominalized clausal passive  
`NUMC` | Compound of numeric modifier (Japanese)  
`COP` | Copula (Spanish)  
`DISLOCATED` | Dislocated relation (for fronted/topicalized elements)  
`ASP` | Aspect marker  
`GMOD` | Genitive modifier  
`GOBJ` | Genitive object  
`INFMOD` | Infinitival modifier  
`MES` | Measure  
`NCOMP` | Nominal complement of a noun  
  
For more information about dependency trees, consult the [Universal Dependency Treebank project](https://github.com/ryanmcd/uni-dep-tb). In addition, [Universal Dependency Annotation for Multilingual Processing](http://www.aclweb.org/anthology/P13-2017) contains background information on the methodology used to interpret such a dependency tree.

## Parsing a syntactic analysis response

The following pseudo-code provides a common pattern to use when performing iterative operations on the syntactic analysis response:
    
    
    index = 0
      for sentence in self.sentences:
        content  = sentence['text']['content']
        sentence_begin = sentence['text']['beginOffset']
        sentence_end = sentence_begin + len(content) - 1
        while index < len(self.tokens) and self.tokens[index]['text']['beginOffset'] <= sentence_end:
          # This token is in this sentence
          index += 1
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
