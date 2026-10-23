---
url: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/summarize-legal-documents/
title: Summarize a legal document \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:56.791079+00:00
---

# Summarize a legal document  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/summarize-legal-documents/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Summarize a legal document Stay organized with collections  Save and categorize content based on your preferences. 

Digest long contracts, depositions, or judicial opinions.

**Note:** Output from Gemini Enterprise is not legal advice. A qualified attorney should review any contract before signature, and should review any summary before it is relied on operationally.

## Example prompt

In the chat box, enter a prompt such as the following:
    
    
    You are a contracts analyst. Attached is the executed master services agreement
    between Cymbal Superstore and Cymbal Consulting, including its exhibits.
    
    Produce an operational summary:
    
    1. **Our obligations** and **their obligations**, in two separate tables. For
    each: what must be done, by when, the triggering event, and the section number.
    
    2. **Dates and deadlines**, in one table: the date or period, what it governs,
    what happens if it is missed, and the section. Include the effective date, the
    term, renewal and notice deadlines, and any deadline measured from an event
    rather than from a fixed date.
    
    3. **Money terms**, quoting verbatim: fees, rate card, payment period, late
    charges, price increase mechanism, and any cap or minimum commitment.
    
    4. **Termination and renewal**, quoting the operative language for each route
    out and the notice each requires.
    
    5. **Defined-term traps.** Any defined term whose contract meaning differs from
    its ordinary meaning in a way that changes how a clause reads.
    
    6. **Ambiguities.** Language that could reasonably be read more than one way.
    Give both readings. Do not choose between them.
    
    7. **Not addressed.** Subjects a reader would expect this agreement to cover
    that it does not.
    
    Rules:
    - Cite a section number for every statement. If you cannot cite one, do not make
    the statement.
    - Quote verbatim for anything involving money, dates, notice, or termination.
    - If the agreement and an exhibit conflict, show both and say they conflict.
    Do not resolve it.
    - Do not give negotiation advice, opinions on whether a term is market, or
    predictions about enforceability.
    - Do not summarize any section you cannot locate in the attached file.
    

## Example output

In response to this prompt, Gemini Enterprise produces output similar to the following:

> ### Our obligations
> 
> Obligation | Deadline | Trigger | Section  
> ---|---|---|---  
> Pay undisputed invoices | 30 days | Receipt of invoice | 4.1  
> Provide system access and a named project contact | 10 business days | Effective date | 3.2  
> Notify of a disputed invoice line | 15 days | Receipt of invoice | 4.5  
> Provide written notice of non-renewal | 60 days before term end | Term end date | 11.2  
>   
> ### Their obligations
> 
> Obligation | Deadline | Trigger | Section  
> ---|---|---|---  
> Deliver a written statement of work before work begins | Before commencement | Each engagement | 2.1  
> Obtain written pre-approval for travel over $2,500 | Before incurring | Travel expense | 6.1  
> Provide monthly written status reports | Monthly | Ongoing | 3.4  
> Return or destroy confidential information | 30 days | Termination or expiry | 9.6  
>   
> ### Dates and deadlines
> 
> Date or period | Governs | If missed | Section  
> ---|---|---|---  
> Effective date: as stated on the signature page | Start of term | - | Preamble  
> Initial term: 3 years | Term | - | 11.1  
> Auto-renewal: successive 1-year terms | Renewal | Renews automatically | 11.2  
> 60 days before term end | Non-renewal notice | Agreement renews for another year | 11.2  
> Net 30 | Payment | Late charge applies, Section 4.4 | 4.1  
> 15 days from invoice | Invoice dispute | Section 4.5 states the line is "deemed accepted" | 4.5  
>   
> **The 60-day non-renewal notice is the deadline most likely to be missed.** It is measured backward from the term end date and the agreement provides no reminder mechanism.
> 
> ### Money terms
> 
> **Section 4.1 (Payment).**
>
>> "Customer shall pay all undisputed amounts within thirty (30) days of receipt of a valid invoice."
> 
> **Section 4.4 (Late charges).**
>
>> "Amounts not paid when due shall accrue interest at one and one-half percent (1.5%) per month or the maximum rate permitted by law, whichever is less."
> 
> **Section 4.6 (Rate adjustment).**
>
>> "Supplier may adjust the rates set forth in Exhibit B upon sixty (60) days' written notice, provided that no adjustment shall exceed five percent (5%) in any twelve (12) month period."
> 
> **Conflict between the agreement and Exhibit B.** Section 4.6 caps annual rate adjustments at 5%. Exhibit B, note 3, states:
>
>> "Rates are subject to annual adjustment in line with the Supplier's then current published rate card."
> 
> These do not say the same thing and the agreement does not state which controls. Flagged for attorney review; not resolved here.
> 
> ### Termination and renewal
> 
> **Section 11.2 (Renewal).**
>
>> "This Agreement shall renew automatically for successive one (1) year terms unless either party provides written notice of non-renewal at least sixty (60) days prior to the end of the then-current term."
> 
> **Section 11.3 (Termination for cause).**
>
>> "Either party may terminate for material breach upon thirty (30) days' written notice if the breach remains uncured at the end of such period."
> 
> **Section 11.4 (Termination for convenience).**
>
>> "Customer may terminate any Statement of Work for convenience upon sixty (60) days' written notice, subject to payment for work performed and non-cancellable commitments incurred through the effective date of termination."
> 
> Termination for convenience applies to a **statement of work** , not to the agreement itself. There is no convenience exit from the master agreement.
> 
> ### Defined-term traps
> 
>   * **"Confidential Information" (1.4)** excludes information "independently developed without reference to the disclosing party's information." That exclusion is broader than the ordinary meaning of the phrase.
>   * **"Deliverable" (1.7)** is limited to items "expressly identified as a Deliverable in a Statement of Work." Work product not named in an SOW is not a Deliverable, which affects the IP assignment in Section 8.
>   * **"Business Day" (1.2)** is defined by reference to the supplier's location, not ours. Every notice period measured in business days runs on their calendar.
> 

> 
> ### Ambiguities
> 
>   * **Section 7.1** requires support "during business hours" without stating a time zone or holiday calendar. Section 1.2 defines "Business Day" but not "business hours." Readable as the supplier's local hours or as ours.
>   * **Section 4.5** says a disputed line is "deemed accepted" after 15 days. It is unclear whether this bars a later challenge to the underlying charge or only to that invoice.
>   * **Section 11.4** refers to "non-cancellable commitments incurred" without defining what qualifies or requiring evidence of them.
> 

> 
> ### Not addressed
> 
> The agreement contains no provision covering:
> 
>   * Data deletion or return on termination, other than the confidentiality obligation in Section 9.6, which addresses confidential information only.
>   * Audit rights.
>   * Subprocessor or subcontractor notification.
>   * Service levels or credits.
>   * Insurance requirements.
> 

> 
> These may appear in a separate document. Nothing in the attached file references one.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
