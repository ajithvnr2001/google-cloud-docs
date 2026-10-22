---
url: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/draft-legal-correspondence/
title: Draft legal correspondence \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:28.948296+00:00
---

# Draft legal correspondence  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/draft-legal-correspondence/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Draft legal correspondence Stay organized with collections  Save and categorize content based on your preferences. 

Explaining a contract clause to a business client means translating what the text actually says, what it means in practice, and where it is genuinely unclear. You can use Gemini Enterprise to draft that explanation from the operative language, with the quoted text attached to every claim you make about it.

**Note:** Output from Gemini Enterprise is not legal advice. A qualified attorney should review any correspondence before it is sent, and should review any contract before signature.

## Example prompt

In the chat box, enter a prompt such as the following:
    
    
    You are a commercial attorney. Attached is our client's supply agreement with
    Cymbal Manufacturing. The client asked whether they can walk away if Cymbal
    misses another delivery date.
    
    Draft an email to the client that:
    
    1. **Quotes the operative language verbatim**, with the section number, before
    explaining anything. Include every section that bears on the answer, including
    cure periods, notice requirements, and any limitation on remedies.
    
    2. **Explains what the text says** in plain language, section by section. State
    only what the words support.
    
    3. **Separates three things explicitly:** what the contract says, what is
    ambiguous, and what I am recommending. Label them.
    
    4. **Identifies the steps that have conditions attached**, such as written
    notice, a cure window, or a deadline measured from a triggering event, and what
    happens if a step is missed.
    
    5. **Lists what you need from the client** to answer the question fully.
    
    Rules:
    - Use only the attached agreement. Do not assume standard terms that aren't in
    this document.
    - Do not predict how a court would rule, characterize the other side's likely
    behavior, or state what remedies are available in law beyond what the contract
    provides.
    - Where language could reasonably be read two ways, say so and give both
    readings. Do not pick one silently.
    - Leave bracketed placeholders for facts I have not given you, such as dates of
    prior missed deliveries. Do not supply plausible values.
    - End with a short list of what I need to confirm before this email goes out.
    

## Example output

In response to this prompt, Gemini Enterprise produces output similar to the following:

> Subject: Your options on the Cymbal delivery delays
> 
> Hi [CLIENT NAME],
> 
> Short answer: the agreement does give you a way out for repeated late delivery, but it is conditional, and the clock on it is shorter than it looks. Here is the language and what it means.
> 
> * * *
> 
> **What the contract says**
> 
> **Section 5.2 (Delivery).**
>
>> "Supplier shall deliver each Order by the delivery date specified in the applicable Purchase Order. Time is of the essence with respect to delivery."
> 
> "Time is of the essence" matters. It means a late delivery is a breach of the agreement on its own, not merely a scheduling problem.
> 
> **Section 12.1 (Termination for cause).**
>
>> "Either party may terminate this Agreement upon thirty (30) days' written notice if the other party commits a material breach and fails to cure such breach within the notice period."
> 
> Termination is not automatic. It requires written notice, and Cymbal gets thirty days to fix the problem after they receive it.
> 
> **Section 12.2 (Repeated failure).**
>
>> "Notwithstanding Section 12.1, Customer may terminate immediately upon written notice if Supplier fails to meet the delivery date for three (3) or more Orders in any rolling six (6) month period."
> 
> This is the provision you are asking about. Three late orders in a rolling six-month window lets you terminate immediately, with no cure period.
> 
> **Section 15.4 (Notices).**
>
>> "All notices shall be in writing and delivered by certified mail or nationally recognized overnight courier to the address set forth in Exhibit A. Notice by email shall not be effective."
> 
> Email does not count. A termination notice sent by email is not valid notice under this agreement.
> 
> * * *
> 
> **What is ambiguous**
> 
>   * **Section 12.2 does not say when the six-month window is measured from.** It can be read as the six months preceding the third missed delivery, or as the six months preceding the notice. If the earlier misses are close to the edge of that window, the two readings give different answers.
>   * **"Fails to meet the delivery date" is not defined.** The agreement does not say whether a partial shipment on time, or a delivery accepted late without objection, counts as a failure. Section 5.2 does not resolve this.
>   * **Section 12.2 does not address whether prior missed deliveries you waived still count.** If your team accepted late deliveries in writing without reserving rights, Cymbal may argue those don't count toward the three.
> 

> 
> * * *
> 
> **What I recommend**
> 
>   1. Before anything else, send written notice by certified mail for the most recent missed delivery, reserving all rights. This preserves your position regardless of which route you take.
>   2. Don't rely on email for anything you may later need to prove as notice.
>   3. Let me confirm the count under Section 12.2 before we act on it. If we are at two rather than three, the immediate-termination route isn't available yet and we should use the Section 12.1 path instead.
> 

> 
> * * *
> 
> **What I need from you**
> 
>   * The dates of each missed delivery in the last six months, and the purchase order number for each. [DATES NOT PROVIDED]
>   * Any written communication where your team accepted a late delivery, agreed to a revised date, or said the delay was acceptable.
>   * Confirmation of the notice address currently in Exhibit A, and whether it has been updated since signing.
>   * Whether you want to preserve the relationship or exit. That changes which of the two termination routes we use.
> 

> 
> Best, [YOUR NAME]
> 
> * * *
> 
> ### Before you send this
> 
>   * Confirm the attached agreement is the executed version and that no amendment or side letter changes Sections 5.2, 12.1, 12.2, or 15.4.
>   * Verify the delivery dates and the count under Section 12.2 yourself; the draft leaves them blank on purpose.
>   * Decide whether to include the recommendation section at all, or to deliver it by phone.
> 


Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
