# AI Contract Intelligence Initiative
### Project Plan — v3 (Current State)

**Strategic Initiative** — links to and enables other executive team projects (see [Strategic Initiative Linkage](#strategic-initiative-linkage))

**Owner:** Jason Yuhas, VP of Commercial Operations  
**Executive Sponsors:** Jen Thomas (CSO) · Chris Jones (CFO)  
**Contributing:** Finance (as directed by Chris Jones) — invoice/billing reconciliation phase  
**Start date:** June 1, 2026  
**Current phase:** Phase 2 — Foundation (W2, W3, W4)  
**Cadence:** Weekly exec slide (Friday) to Executive Team + SLT  
**Last Updated:** July 29, 2026

---

## Current State & Immediate Milestones

| Milestone | Target | Notes |
|---|---|---|
| **W1–W4 initial assessment** | **Friday, Aug 1, 2026** | Summary of progress across W1–W4. Missing data is **not punitive** — the goal is to see where we have holes and gaps. Gaps are expected outputs, not failures. |
| **W5 kickoff** | **This week (week of Jul 29)** | Must start now. First focus: **unique identifiers** for invoice-to-SOW linkage. W1–W4 assessment gates full W5 execution, not W5 setup. |

> **Phase 2 objective:** Complete foundational contract intelligence (W2–W4) with an honest gap assessment by Friday, while standing up W5 identifier schema in parallel.

---

## Purpose

This is not a cleanup project. It is a **CipherHealth strategic initiative** — a foundational capability for AI RevOps maturity and a strategic asset for **Sales, Finance, Legal, Customer Success, and Product**.

The end state is an **AI-powered contract intelligence repository**, not a document library.

**Downstream value:** strategic account planning, renewal management, pricing governance, expansion identification, forecasting, and automation.

**Guiding principle:** AI accelerates the work; all outputs are **trust, but verify**. The objective is strategic account planning — not legal interpretation.

---

## Strategic Initiative Linkage

**AI Contract Intelligence is its own strategic initiative.** It does not sit underneath Product Naming or Pricing & Packaging — it **links to and enables** them (and others across the executive team portfolio) by establishing the ground-truth contract dataset.

| Linked Initiative | Executive Owner / Domain | What AI Contract Intelligence Provides | Dependency Direction |
|---|---|---|---|
| **Product Naming** (Cipher → Evolve → Catalyst → Outreach / Rounding) | Product | Ground-truth inventory of product names, modules, and packages actually contracted across 77 customers. Required before reconciling contracted names to the 2026 product hierarchy or migrating customers to new naming. | Product Naming **depends on** W3/W4 baseline |
| **Pricing & Packaging** | Product · Finance | Complete view of contracted price, referenced future pricing, utilization commitments, and package composition. The dataset needed to design future packages and govern pricing exceptions. | Pricing & Packaging **depends on** W3/W4/W5 baseline |
| **GRR / Renewal Management** | CS · Sales | Renewal dates, notice windows, auto-renewal terms, and TFC provisions feed the 12-month rolling renewal calendar. Directly supports GRR recovery and churn prevention. | GRR **depends on** W3/W4; W6 automation inherits |
| **AI RevOps Maturity** | Sales · Finance · RevOps | Foundational contract intelligence layer for AI-assisted account planning, forecasting, and workflow automation across the revenue org. | AI RevOps **enabled by** full initiative |
| **Billing & Revenue Integrity** | Finance (Chris Jones) | Contracted vs. deployed vs. billed view (W5). Surfaces change orders, adds, price increases, and billing exposure. Supports revenue recognition and audit readiness. | Finance **depends on** W5 |
| **Security & Compliance Posture** | Legal · Security | Contract metadata, assessment currency, and commercial restriction visibility (logo/marketing/reference). Dated assessments create pipeline and churn risk. | Security **inherits from** W3 metadata |
| **CRM & Account Hierarchy** | Sales · RevOps | Parent-child account hierarchy, contracted entitlements, and renewal data aligned to account records. | Account hygiene **depends on** W2–W4/W5 IDs |
| **Legal / Commercial Operations** | Legal | MSA summaries, order of precedence, non-standard amendment flags. Trust-but-verify drafts — strategic planning, not legal interpretation. | Legal **consumes** W3/W4 outputs |
| **Customer Success / Deployment Alignment** | CS · Professional Services | Contracted vs. deployed comparison — programs, workflows, use cases, volumes. Identifies entitlement gaps and expansion whitespace. | CS **depends on** W4; validated in W5 |

---

## Sequencing & Phase Status

| Phase | Timing | Workstreams | Status |
|---|---|---|---|
| **Phase 1 — Kickoff** | Jun 1 – Jun 30 | W1 stood up, W2 begins | **Complete** |
| **Phase 2 — Foundation** | Jul 1 – Aug 15 | W2, W3, W4 in parallel; W1 reporting ongoing | **In progress** — W1–W4 assessment due Aug 1 |
| **Phase 3 — Reconciliation** | Starting Jul 29 (W5 setup); full execution after Aug 1 assessment | W5 begins — unique identifiers this week | **Starting this week** |
| **Phase 4 — Automation eval** | Aug 15+ | W6 — cross-functional discussion | Not started |

> Cross-functional automation discussions (W6) begin **after** the foundational data set is clean — not before.

---

## Workstreams

Each workstream is scoped so progress can be reported on a single exec slide.

---

### W1 — Weekly Cadence & Reporting Rhythm
**Owner:** Jason Yuhas | **Status:** Active

AI-generated weekly progress slide, delivered every **Friday** to Executive Team + SLT. Each slide is **standalone-readable** — anyone in SLT viewing a single week's slide should immediately understand what the initiative is, why it matters, current progress, and — critically — what the work is *surfacing* about business operations continuity risk and opportunity. AI-automated after week 2.

**Friday Aug 1 deliverable:** Initial W1–W4 assessment slide — overall % complete, gap summary, and hole inventory (non-punitive).

---

### W2 — Contract Repository (77 Contracts)
**Owner:** Jason Yuhas | **Status:** In progress (Phase 2)

- Centralize all executed agreements in a single repository, organized by parent organization
- Establish and document the long-term storage location and naming convention
- Every document searchable and AI-ready
- Version control: current executed versions clearly distinguished from superseded documents

**Deliverables:**
- [ ] Central contract repository populated with all 77 executed agreements
- [ ] Parent-organization hierarchy documented
- [ ] Storage location and naming convention documented (runbook)
- [ ] Documents indexed for search and AI ingestion
- [ ] Version policy enforced: executed vs. redline vs. superseded
- [ ] **Aug 1:** Gap report — which contracts are missing, incomplete, or lack executed version clarity

---

### W3 — MSA Summaries
**Owner:** Jason Yuhas (AI-assisted via Cursor) | **Status:** In progress (Phase 2)

**Version control requirement:** AI must only read **current, executed versions** of MSAs — not documents passed during redlines, and not versions that have been replaced or updated.

Standardized summary per customer capturing:
- MSA title
- Parent organization and covered entities
- Whether MSA extends to child accounts / affiliates *(flags expansion opportunities)*
- Signature date and customer signer
- Order of precedence
- Contract term
- Renewal date and renewal language *(including agreements that remain active while an SOW is active)*
- Notable commercial, legal, or operational provisions with account strategy impact
- Restrictions — logo usage, marketing, reference use *(AI can scan for these)*

**Objective:** Strategic account planning, not legal interpretation. Trust but verify.

- [ ] **Aug 1:** Summary completion status + field-level gap inventory per customer

---

### W4 — Active SOW Inventory
**Owner:** Jason Yuhas | **Status:** In progress (Phase 2)

Per active SOW:
- Product names / modules purchased
- Programs, workflows, and use cases deployed
- Scripts / campaign details where applicable
- Contracted volumes and utilization commitments
- Contracted pricing
- Referenced future pricing
- Go-live date
- Termination-for-convenience provisions
- Auto-renewal terms and notice requirements
- **Non-standard amendments** — exceptions or commercial changes executed via email or other side-channel means. **Flag separately.**

- [ ] **Aug 1:** SOW coverage report — which active SOWs are complete vs. partial vs. not started

---

### W5 — Invoice-to-SOW Reconciliation
**Executive Sponsor:** Chris Jones (CFO) | **Contributing:** Finance (as directed by Chris Jones)  
**Sequenced:** Setup starts **this week**; full reconciliation proceeds after Aug 1 W1–W4 assessment

Connect latest invoice detail to each active SOW so we have one view of **contracted vs. deployed vs. billed**. Cross-functional touchpoints with Finance.

**This week (W5 kickoff) — unique identifiers:**
- [ ] Establish **unique identifiers** that tie invoice line items → SOW → parent account → MSA
- [ ] Document identifier schema and mapping rules (Finance + Jason)

**Expected variance — not a failure condition:** Initial SOW records will not always match invoice detail. Common drivers include change orders, adds, and price increases executed after the original SOW. These variances are **outputs of the work** — they surface pricing governance gaps and billing exposure, not blockers to progress.

**Deliverables:**
- [ ] Unique identifier schema documented and agreed (this week)
- [ ] Invoice-to-SOW mapping for all active accounts
- [ ] Discrepancy report (contracted vs. deployed vs. billed)
- [ ] Change order / add / price increase log linked to variance items

---

### W6 — AI Automation Layer (Future Phase)
**Sequenced:** After foundational data set is clean (Phase 4)

Evaluate where AI automation adds value — renewal notifications, workflow orchestration, rolling 12-month renewal calendar. Cross-functional teams (CS, Finance, Legal, Product) engaged **after** this foundational work, not before.

---

## Repository Home — Decision

**Interim (W2–W5):** Google Drive. Parent-org folder structure with disciplined naming, documented as part of W2. Already in use, no procurement cycle, plays cleanly with Cursor and existing AI tooling. Sufficient to support the repository, MSA/SOW summarization, and invoice reconciliation phases.

**Long-term platform evaluation:** Deferred to W6 kickoff — not before. Rationale: we should not evaluate long-term contract management platforms while still discovering what "good" contract metadata looks like for CipherHealth. The MSA and SOW summarization work will reveal the actual field set that matters — *that* becomes the requirements doc.

---

## Weekly Exec Slide Template (W1 Output)

One page. Standalone-readable — an SLT member viewing any single week should understand the project, its purpose, current state, and what it is surfacing.

**Structure:**

- **Header:** Week of [date] · AI Contract Intelligence Initiative

- **Project & Why** (2 lines, appears every week)
  - *What:* Building an AI-powered contract intelligence repository across our 77 executed customer agreements.
  - *Why:* A CipherHealth strategic initiative — foundational to account planning, renewal governance, pricing baseline, and linked executive projects (Product Naming, Pricing & Packaging, GRR, Billing Integrity).

- **Overall % Complete** — progress bar, 77-contract denominator

- **Key Accomplishments** — 3–5 bullets

- **Gap Inventory — Where We Have Holes** *(non-punitive; expected)*  
  Missing contracts, incomplete MSA fields, SOWs not inventoried, identifier gaps. Surfaces blind spots — outputs of the work.

- **Risks Surfaced — Business Operations Continuity**  
  Risks discovered *through* the work this week — distinct from project blockers.

- **Opportunities Identified — Continuity of Business Operations**  
  Improvements the work is revealing.

- **Blockers · Decisions Needed** — project-level, cross-functional

- **Remaining Work + Projected Completion**

- **Linked Strategic Initiative Progress** — one line each on Product Naming, Pricing & Packaging, GRR, and Billing Integrity baselines

> By week 4, *Gap Inventory*, *Risks Surfaced*, and *Opportunities Identified* become the compounding operational value — not just status, but business intelligence.

---

## Guardrails

- **HIPAA:** Contract metadata only — no PHI in AI prompts or outputs.
- **Trust but verify:** AI accelerates the work; humans validate. All outputs are drafts until reviewed.
- **Gaps are the point:** We expect them. Missing data is **not punitive**. Gaps identify blind spots — they are outputs of the work, not blockers to it.
- **Version integrity:** AI ingests executed agreements only — never redlines or superseded versions.
- **SOW-invoice variance:** Mismatch between SOW and invoice is expected initially; document change orders, adds, and price increases rather than forcing false alignment.

---

## Stakeholders & Roles

| Role | Name | Responsibility |
|---|---|---|
| **Owner** | Jason Yuhas, VP of Commercial Operations | Overall delivery, W1–W4, W6 coordination |
| **Executive Sponsor** | Jen Thomas (CSO) | Priority setting, Sales/RevOps alignment, cross-functional escalation |
| **Executive Co-Sponsor** | Chris Jones (CFO) | Finance alignment, W5 sponsorship, billing integrity |
| **Finance Support** | Finance (as directed by Chris Jones) | W5 — invoice-to-SOW linkage, unique identifier schema |
| **SLT / Executive Team** | — | Weekly slide visibility (Fridays) |
| **Sales, Finance, Legal, CS, Product** | — | W6 cross-functional input; trust-but-verify on outputs |

---

## Open Questions — Active

- ~~Final choice of repository location~~ — *interim: Google Drive (decided)*
- Cursor/AI tooling setup and access for Jason's team
- Definition of "active" for SOW inventory (W4) — treatment of expired-but-still-invoicing agreements
- **Unique identifier schema** — invoice line → SOW → account → MSA crosswalk (this week)

---

## Definition of Done — Initiative Complete

1. All 77 contracts centralized, searchable, and AI-ready (current executed versions only)
2. Every customer has a verified MSA summary — including logo, marketing, and reference restrictions
3. Every active SOW has a complete inventory record with exceptions flagged separately
4. Weekly AI-assisted exec slide operational and delivering business intelligence (including gap inventory)
5. Invoice details linked to active SOWs via unique identifiers with documented variance explanations
6. Linked strategic initiatives (Product Naming, Pricing & Packaging, GRR, Billing Integrity) have a trusted baseline dataset
7. Long-term platform requirements defined from discovered metadata (W6 trigger)
8. Repository functions as an **AI-powered contract intelligence platform** — not a passive document library

---

*v3 — Updated for current state: started Jun 1, Phase 2 in progress, Aug 1 assessment, W5 kickoff this week.*
