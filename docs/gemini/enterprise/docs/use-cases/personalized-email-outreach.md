---
url: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/personalized-email-outreach/
title: Write a personalized outreach email \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:57.082795+00:00
---

# Write a personalized outreach email  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/personalized-email-outreach/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Write a personalized outreach email Stay organized with collections  Save and categorize content based on your preferences. 

Personalizing an outreach email can fail in two ways: an email can say nothing specific about the prospect, or the email can say something specific and wrong. You can use Gemini Enterprise to research an account, draft outreach grounded in the research, and separate the claims you can source from the ones you can't.

The research and the drafting are two different jobs. Run the research first with the Deep Research agent, which produces a cited report, then bring that report into the Gemini Enterprise chat to draft from.

## Before you begin

  * To research a public company, select the **Deep Research** agent rather than asking the assistant to "do deep research" in a normal chat turn.
  * Attach your own product collateral to give the assistant specific product knowledge.
  * Personal profile pages on social networks are usually not retrievable. If a person's background matters, paste the relevant text into the prompt instead of linking to it. 
    * Researching a named individual may be subject to your organization's privacy and data-handling policies.



## Example prompt

Select the Deep Research agent, and enter a prompt such as the following:
    
    
    Research Cymbal Retail Group, a public specialty retailer, for a sales
    conversation. I want:
    
    1. Their stated strategic priorities for this fiscal year, in their own words,
    with a source for each.
    
    2. Operational problems they have publicly acknowledged, from earnings calls,
    annual reports, or press coverage. Quote them.
    
    3. Recent changes in leadership, structure, or technology spending.
    
    4. Anything that would make this a bad time to reach out.
    
    Cite a source for every claim. If something is widely repeated but you cannot
    find a primary source, say so.
    

Then, in the Gemini Enterprise chat box, enter a prompt such as the following:
    
    
    Using the research report above and the attached product one-pager for our
    inventory forecasting platform, draft a first outreach email to the VP of
    Supply Chain at Cymbal Retail Group.
    
    Requirements:
    
    1. **Under 150 words.** No greeting paragraph about how much I admire their
    company.
    
    2. **One specific observation about their business**, drawn from the research
    and traceable to a source. Not a generic industry statement.
    
    3. **One connection to what we do**, using only capabilities stated in the
    attached one-pager.
    
    4. **A low-commitment ask.** Not a demo request.
    
    Then, separately from the email:
    
    5. **A source table:** every factual claim in the email, and where it came from.
    
    6. **Claims I should verify before sending**, including anything sourced from a
    secondary report rather than the company itself.
    
    Rules:
    - Do not state anything about our product that is not in the attached
    one-pager. If the natural thing to say isn't in there, write [NOT IN
    COLLATERAL] and tell me what claim you wanted to make.
    - Do not attribute a quote or a priority to an individual unless the source
    attributes it to that individual by name.
    - Do not describe their current tools or vendors unless a source states them.
    

## Example output

In response to the drafting prompt, Gemini Enterprise produces output similar to the following:

> **Subject: Your Q3 comment on peak-season stockouts**
> 
> Hi [NAME],
> 
> On the Q3 call, your CFO said stockouts during peak "cost us more in lost sales than the markdowns did." That's a hard problem to fix with more safety stock, since it usually just moves the cost to the other side of the ledger.
> 
> We build inventory forecasting that models promotional lift separately from baseline demand, which is typically where peak forecasts break down. Two of our customers are specialty retailers of roughly your store count.
> 
> Worth 20 minutes to compare notes on how you're handling peak forecasting today? Happy to share what we've seen work even if we're not a fit.
> 
> [YOUR NAME]
> 
> * * *
> 
> ### Source table
> 
> Claim in the email | Source  
> ---|---  
> CFO comment on peak stockouts | Q3 earnings call transcript, prepared remarks — quoted verbatim  
> They are a specialty retailer with a comparable store count | Annual report, store count disclosure  
> We model promotional lift separately from baseline demand | Attached one-pager, "Demand decomposition" section  
> Two customers of similar profile | Attached one-pager, customer summary page  
>   
> ### Claims to verify before sending
> 
>   * **The CFO quote is verbatim and attributed correctly** , but confirm it was the CFO and not the COO. The transcript attribution is clear; the secondary coverage I found attributed it to "management."
>   * **"Two of our customers are specialty retailers of roughly your store count"** comes from the one-pager. Confirm you're allowed to reference them, even unnamed, in outbound email.
>   * **[NOT IN COLLATERAL]** I wanted to say our forecasts improve peak accuracy by a specific percentage, because that would be the strongest line in the email. The one-pager contains no accuracy figure. If a defensible number exists, add it and I'll rewrite around it.
> 

> 
> ### What I deliberately left out
> 
>   * A trade-press article claimed they are replacing their planning system this year. No company source confirms it, and being wrong about a prospect's stack in a first email is expensive. Omitted.
>   * The VP's background. Their profile page could not be retrieved, so nothing in this email refers to them personally.
> 


Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
