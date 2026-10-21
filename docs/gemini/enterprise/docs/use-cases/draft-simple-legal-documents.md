---
url: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/draft-simple-legal-documents/
title: Draft a first pass at a routine legal document \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:21:34.892053+00:00
---

# Draft a first pass at a routine legal document  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/draft-simple-legal-documents/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Draft a first pass at a routine legal document Stay organized with collections  Save and categorize content based on your preferences. 

Routine documents follow a known shape, and the slowest part of the process is assembling the facts. You can use Gemini Enterprise to produce a first draft that leaves every fact you didn't supply as a visible placeholder, so the gaps are obvious rather than filled in with something plausible.

**Note:** Output from Gemini Enterprise is not legal advice. A qualified attorney must review and revise any document before it is sent, filed, or signed, and should review any contract before signature. Don't send output from Gemini Enterprise to a third party without attorney review.

## Example prompt

In the chat box, enter a prompt such as the following:
    
    
    You are a paralegal preparing a first draft for attorney review. Draft a cease
    and desist letter.
    
    Facts I am giving you, and the only facts you may treat as established:
    - Our client is Cymbal Superstore.
    - Cymbal Superstore uses the mark "CYMBAL" in connection with retail store
      services.
    - The recipient is Cadence Retail Group, operating a store under the name
      "Cymbal Outlet" in the same metropolitan area.
    - Our client first learned of the recipient's use on \[DATE\].
    
    Draft the letter with:
    
    1. Identification of the parties and the mark, using only the facts above.
    
    2. A description of the conduct we are objecting to.
    
    3. The demands: stop using the name, confirm in writing within a stated period,
    and provide an accounting of use to date.
    
    4. A closing that reserves all rights.
    
    Rules:
    - Do not assert any fact I have not given you. This includes registration
    status, registration numbers, the date of first use, the goods or services the
    recipient offers, sales figures, and whether anyone has been confused.
    - Do not cite any statute, case, or regulation. Insert [CITE - ATTORNEY TO
      SUPPLY] where authority belongs.
    - Do not state legal conclusions such as that infringement has occurred, that
      the mark is famous, or that a likelihood of confusion exists. Describe the
      conduct and the objection instead.
    - Use a bracketed placeholder in ALL CAPS for every unknown, and use the same
      placeholder text for the same fact throughout.
    - Do not assume a jurisdiction or governing law.
    
    After the draft, give me three lists: assumptions you deliberately did not make,
    facts still needed, and determinations that require an attorney.
    

## Example output

In response to this prompt, Gemini Enterprise produces output similar to the following:

> [FIRM LETTERHEAD]
> 
> [DATE]
> 
> **VIA [DELIVERY METHOD - ATTORNEY TO SPECIFY]**
> 
> Cadence Retail Group [RECIPIENT ADDRESS]
> 
> **Re: Use of "Cymbal Outlet"**
> 
> Dear [RECIPIENT CONTACT NAME]:
> 
> This firm represents Cymbal Superstore. Cymbal Superstore uses the mark CYMBAL in connection with retail store services.
> 
> It has come to our client's attention that Cadence Retail Group is operating a retail location under the name "Cymbal Outlet" at [RECIPIENT LOCATION ADDRESS], in the same metropolitan area in which our client operates. Our client first became aware of this use on [DATE CLIENT LEARNED OF USE].
> 
> Our client objects to this use. [BASIS FOR OBJECTION - ATTORNEY TO STATE, WITH CITE - ATTORNEY TO SUPPLY.]
> 
> Accordingly, we request that Cadence Retail Group:
> 
>   1. Immediately cease all use of "Cymbal Outlet" and of any other name or mark incorporating "CYMBAL" in connection with retail store services, including use in signage, advertising, packaging, online listings, social media, and domain names;
> 
>   2. Confirm in writing within [NUMBER] days of the date of this letter that it has done so and will not resume such use; and
> 
>   3. Provide an accounting of its use of the name to date, including the date use began, the locations and channels in which the name has been used, and [ADDITIONAL ACCOUNTING ITEMS - ATTORNEY TO SPECIFY].
> 
> 

> 
> Nothing in this letter constitutes a waiver of any right or remedy available to our client, all of which are expressly reserved.
> 
> Please direct your response to the undersigned.
> 
> Sincerely,
> 
> [ATTORNEY NAME] [FIRM NAME]
> 
> * * *
> 
> ### Assumptions I deliberately did not make
> 
>   * **Registration status.** You told me our client uses the mark. You did not tell me it is registered, where, or under what number. The letter says "uses" and nothing more. If the mark is registered, that fact and the registration number should be added, and the objection paragraph will likely change.
>   * **What the recipient sells.** You gave me a store name and a location, not the goods or services offered. The letter does not claim the parties' services overlap.
>   * **Priority.** Nothing here states who used the name first. That is typically the pivotal fact and it is not in what you gave me.
>   * **Actual confusion.** No incident of confusion was described, so none is alleged.
>   * **Jurisdiction and governing law.** Not stated, so no forum, statute, or body of law is referenced anywhere in the draft.
> 

> 
> ### Facts still needed
> 
>   * Date of the client's first use of CYMBAL in this geographic area, and evidence of that use.
>   * Registration status and number, if any, and the classes covered.
>   * The recipient's date of first use, if known, and how you learned of it.
>   * The recipient's legal entity name, registered agent, and address for service.
>   * Whether the parties have had any prior contact about this name.
>   * Any instances of actual confusion, and how they were documented.
>   * The response deadline you want, and the delivery method.
> 

> 
> ### Determinations that require an attorney
> 
>   * Whether to send this letter at all, given that a demand letter can precipitate a declaratory judgment action.
>   * The legal basis for the objection and the authority to cite.
>   * Whether the demands are proportionate, and whether the accounting request should be included in a first letter.
>   * The tone: this draft is deliberately neutral. Escalating it is a judgment call.
>   * Whether any of the placeholders above should remain blank as a matter of strategy rather than being filled in.
> 


Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
