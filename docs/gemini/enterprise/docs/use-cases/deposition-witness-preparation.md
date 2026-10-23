---
url: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/deposition-witness-preparation/
title: Prepare for a deposition \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:12.329287+00:00
---

# Prepare for a deposition  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/deposition-witness-preparation/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Prepare for a deposition Stay organized with collections  Save and categorize content based on your preferences. 

Prepare for a deposition by building a witness's documentary footprint from the case file and turning it into an outline where every line of questioning is tied to an exhibit.

**Note:** Output from Gemini Enterprise is not legal advice. A qualified attorney must review and verify any deposition outline, and confirm every document reference against the record.

## Example prompt

In the chat box, enter a prompt such as the following:
    
    
    You are a litigation associate preparing to depose the opposing party's
    operations manager. Attached are the complaint, the answer, the parties'
    agreement, the produced email set, and the transcript of the plant supervisor's
    deposition.
    
    Build a preparation packet:
    
    1. **Witness footprint.** Every document in the attached record that this
    witness authored, received, or is named in. Give the date, the document, the
    Bates or exhibit number as it appears in the file, and one line on why it
    matters. Order by date.
    
    2. **Contradictions.** Any place this witness's documents conflict with the
    plant supervisor's testimony, with the other party's pleadings, or with each
    other. Quote both sides verbatim and cite each.
    
    3. **Outline by topic.** For each topic, give the fact you are trying to
    establish, the document you would use to establish it, and three to five
    questions building to it. Every question must be answerable from a document in
    the attached record.
    
    4. **Anticipated problems.** Areas where the record is favorable to the witness,
    and what they are likely to say.
    
    5. **Not in the record.** Facts the pleadings assume that no attached document
    supports. These are the questions where you have no exhibit to fall back on.
    
    Rules:
    - Use only the attached documents. Do not invent exhibit numbers, Bates numbers,
      dates, names, or quotes.
    - Quote verbatim when you say a document says something, and cite it.
    - If you cannot support a line of questioning from the record, put it under "Not
      in the record" rather than writing the question as though you can.
    - Use bracketed placeholders such as [DATE NOT IN RECORD] rather than filling
      in a plausible value.
    

## Example output

In response to this prompt, Gemini Enterprise produces output similar to the following:

> ### Witness footprint
> 
> Date | Document | Cite | Why it matters  
> ---|---|---|---  
> Mar 4 | Email, witness to plant supervisor | CYM-000412 | Directs a change to the inspection interval three weeks before the failure  
> Mar 19 | Weekly operations report, authored by witness | CYM-000871 | Reports "no open maintenance items" for the affected line  
> Apr 2 | Email chain, witness copied | CYM-001033 | Supervisor raises a vibration complaint; witness does not reply on the chain  
> Apr 11 | Incident summary, authored by witness | CYM-001190 | States the failure was "sudden and without prior indication"  
>   
> ### Contradictions
> 
> **The Apr 11 incident summary against the Apr 2 email.**
> 
> The witness wrote on April 11 (CYM-001190):
>
>> "The failure was sudden and without prior indication."
> 
> The witness was copied on April 2 (CYM-001033), where the supervisor wrote:
>
>> "Line 3 is vibrating again, worse than last month. We should look at it before the next run."
> 
> **The Mar 19 report against the supervisor's testimony.**
> 
> The witness's March 19 report states "no open maintenance items." The supervisor testified (Dep. 84:6-14):
>
>> "I told him the bearing needed replacing. I told him more than once."
> 
> ### Outline by topic
> 
> **Topic 1: The witness received notice of the vibration.** Fact to establish: the witness saw the April 2 email. Document: CYM-001033.
> 
>   1. You use the email address shown at the top of this document?
>   2. Reading the recipient line, you were copied on this message?
>   3. Do you have any reason to believe you did not receive it?
>   4. You did not reply to this message, correct?
>   5. Did you take any action in response to it?
> 

> 
> **Topic 2: The inspection interval changed before the failure.** Fact to establish: the witness directed the change. Document: CYM-000412.
> 
>   1. This is an email you sent on March 4?
>   2. Please read the second sentence aloud.
>   3. Who decided to make that change?
>   4. What was the interval before this email?
>   5. Was anyone consulted before the change?
> 

> 
> ### Anticipated problems
> 
>   * **The March 19 report may not be the witness's own work.** The document carries no signature block and the record does not establish who compiled it. Expect "that report is assembled by the shift leads." Establish authorship before using it.
>   * **"Without prior indication" is arguably about the mechanical failure rather than the complaint history.** Expect the witness to draw that distinction. Pin down what they understood the phrase to mean at the time.
> 

> 
> ### Not in the record
> 
>   * Nothing in the attached documents shows what the inspection interval was changed **to** , or who approved the change. The complaint asserts it doubled; no attached document states that. [NOT IN RECORD - confirm before asking a question that assumes it.]
>   * No maintenance log, work order, or bearing replacement record appears in the production. If one exists, it is the central document for Topic 2 and is missing.
>   * The supervisor's testimony refers to telling the witness "more than once." Only one written instance appears in the record. [DATES OF OTHER INSTANCES NOT IN RECORD.]
> 


Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
