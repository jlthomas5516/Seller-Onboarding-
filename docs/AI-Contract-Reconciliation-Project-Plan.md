# AI Contract Intelligence Initiative
### Project Plan — v2 (Merged Executive + Operational)

**Owner:** Jason Yuhas, SVP Strategic Accounts  
**Executive Sponsor:** Jen Thomas, CSO  
**Contributing:** Chris Peak (CRE) — invoice/billing reconciliation phase  
**Initial summary due:** Friday, August 1, 2026  
**Cadence:** Weekly exec slide (Friday) to Executive Team + SLT  
**Last Updated:** July 29, 2026

---

## Purpose

This is not a cleanup project. It is a foundational capability for CipherHealth's AI RevOps maturity — a strategic asset that will serve **Sales, Finance, Legal, Customer Success, and Product**.

The end state is an **AI-powered contract intelligence repository**, not a document library.

**Downstream value:** strategic account planning, renewal management, pricing governance, expansion identification, forecasting, and automation.

**Guiding principle:** AI accelerates the work; all outputs are **trust, but verify**. The objective is strategic account planning — not legal interpretation.

---

## Strategic Initiative Linkage

This work establishes the baseline dataset that active strategic initiatives depend on:

| Strategic Initiative | What This Initiative Provides |
|---|---|
| **Product Naming** (Cipher → Evolve → Catalyst → Outreach / Rounding) | Ground-truth inventory of product names, modules, and packages actually contracted across 77 customers. Required before reconciling contracted names to the 2026 product hierarchy or migrating customers to new naming. |
| **Pricing & Packaging** | Complete view of contracted price, referenced future pricing, utilization commitments, and package composition across the customer base. The dataset the pricing & packaging strategic initiative needs to design future packages. |
| **GRR / Renewal Management** (secondary) | Renewal dates, notice windows, auto-renewal terms, and TFC provisions feed the 12-month rolling renewal calendar. Directly supports GRR recovery. |

---

## Sequencing

| Phase | Timing | Workstreams |
|---|---|---|
| Kickoff | Week of Jul 27 | W1 stood up, W2 begins |
| Foundation | Weeks 2–4 | W2, W3, W4 in parallel |
| Reconciliation | Weeks 5–6 | W5 begins (Chris Peak) |
| Automation eval | Week 7+ | W6 — cross-functional discussion |

> Cross-functional automation discussions (W6) begin **after** the foundational data set is clean — not before.

---

## Workstreams

Each workstream is scoped so progress can be reported on a single exec slide.

---

### W1 — Weekly Cadence & Reporting Rhythm
**Owner:** Jason Yuhas | **Status:** Establishing this week

AI-generated weekly progress slide, delivered every **Friday** to Executive Team + SLT. Each slide is **standalone-readable** — anyone in SLT viewing a single week's slide should immediately understand what the initiative is, why it matters, current progress, and — critically — what the work is *surfacing* about business operations continuity risk and opportunity. Format standardized (see template below). AI-automated after week 2.

---

### W2 — Contract Repository (77 Contracts)
**Owner:** Jason Yuhas | **Status:** Kicking off

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

---

### W3 — MSA Summaries
**Owner:** Jason Yuhas (AI-assisted via Cursor)

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

---

### W4 — Active SOW Inventory
**Owner:** Jason Yuhas

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

---

### W5 — Invoice-to-SOW Reconciliation
**Owner:** Chris Peak (CRE) | **Sequenced:** After W2–W4 stable

Connect latest invoice detail to each active SOW so we have one view of **contracted vs. deployed vs. billed**. Cross-functional touchpoints with Finance.

**Expected variance — not a failure condition:** Initial SOW records will not always match invoice detail. Common drivers include change orders, adds, and price increases executed after the original SOW. These variances are **outputs of the work** — they surface pricing governance gaps and billing exposure, not blockers to progress.

**Deliverables:**
- [ ] Invoice-to-SOW mapping for all active accounts
- [ ] Discrepancy report (contracted vs. deployed vs. billed)
- [ ] Change order / add / price increase log linked to variance items

---

### W6 — AI Automation Layer (Future Phase)
**Sequenced:** After foundational data set is clean (Week 7+)

Evaluate where AI automation adds value — renewal notifications, workflow orchestration, rolling 12-month renewal calendar. Cross-functional teams (CS, Finance, Legal, Product) engaged **after** this foundational work, not before.

---

## Repository Home — Decision

**Interim (W2–W5):** Google Drive. Parent-org folder structure with disciplined naming, documented as part of W2. Already in use, no procurement cycle, plays cleanly with Cursor and existing AI tooling. Sufficient to support the repository, MSA/SOW summarization, and invoice reconciliation phases.

**Long-term evaluation trigger:** W6 kickoff — not before. Rationale: we should not shop for a CLM while still discovering what "good" contract metadata looks like for CipherHealth. The MSA and SOW summarization work will reveal the actual field set that matters — *that* becomes the CLM requirements doc.

**CLM evaluation criteria (when triggered):**
- Native AI-assisted metadata extraction (not bolted on)
- API access for downstream integration — Salesforce, billing, renewal workflows
- "Contracted vs. deployed vs. billed" reporting inherited from W5
- Rolling renewal calendar and notification workflows for W6
- Parent-child organizational hierarchy support
- Cost modeled at 77-contract scale + projected growth
- Salesforce-native path worth evaluating (Files Connect, AppExchange CLM) given Salesforce is our system of record

**Candidates worth benchmarking:** Ironclad, LinkSquares, Agiloft, Icertis.

---

## Weekly Exec Slide Template (W1 Output)

One page. Standalone-readable — an SLT member viewing any single week should understand the project, its purpose, current state, and what it is surfacing.

**Structure:**

- **Header:** Week of [date] · AI Contract Intelligence Initiative

- **Project & Why** (2 lines, appears every week)
  - *What:* Building an AI-powered contract intelligence repository across our 77 executed customer agreements.
  - *Why:* Foundational to strategic account planning, renewal governance, pricing baseline, and the product naming and pricing/packaging strategic initiatives.

- **Overall % Complete** — progress bar, 77-contract denominator

- **Key Accomplishments** — 3–5 bullets

- **Risks Surfaced — Business Operations Continuity**  
  Risks discovered *through* the work this week — distinct from project blockers.  
  Examples: unclear renewal language, missed TFC clauses, non-standard amendments creating billing exposure, orphaned SOWs, undocumented pricing exceptions, marketing/logo restrictions we've been violating, auto-renewal notice windows already inside the trigger date.

- **Opportunities Identified — Continuity of Business Operations**  
  Improvements the work is revealing.  
  Examples: renewal automation candidates, package standardization opportunities, pricing governance gaps, expansion signals from MSA affiliate clauses, cross-sell whitespace visible from contracted-vs-deployed comparison.

- **Blockers · Decisions Needed** — project-level, cross-functional

- **Remaining Work + Projected Completion**

- **Strategic Initiative Progress** — one line each on Product Naming baseline and Pricing / Packaging baseline

> By week 4, the *Risks Surfaced* and *Opportunities Identified* sections become the compounding operational value of the initiative — not just status, but business intelligence.

---

## Guardrails

- **HIPAA:** Contract metadata only — no PHI in AI prompts or outputs.
- **Trust but verify:** AI accelerates the work; humans validate. All outputs are drafts until reviewed.
- **Gaps are the point:** We expect them. Gaps identify our blind spots — they are outputs of the work, not blockers to it.
- **Version integrity:** AI ingests executed agreements only — never redlines or superseded versions.
- **SOW-invoice variance:** Mismatch between SOW and invoice is expected initially; document change orders, adds, and price increases rather than forcing false alignment.

---

## Stakeholders & Roles

| Role | Name | Responsibility |
|---|---|---|
| **Owner** | Jason Yuhas | Overall delivery, W1–W4, W6 coordination |
| **Executive Sponsor** | Jen Thomas (CSO) | Priority setting, cross-functional escalation |
| **Billing Reconciliation** | Chris Peak (CRE) | W5 — invoice-to-SOW linkage |
| **SLT / Executive Team** | — | Weekly slide visibility (Fridays) |
| **Sales, Finance, Legal, CS, Product** | — | W6 cross-functional input; trust-but-verify on outputs |

---

## Open Questions for Kickoff

- Final choice of repository location and naming convention (W2) — *interim decision: Google Drive*
- Cursor/AI tooling setup and access for Jason's team
- Definition of "active" for SOW inventory (W4) — treatment of expired-but-still-invoicing agreements
- Cadence handoff point for W5 (Chris Peak) — trigger criteria for start

---

## Definition of Done — Initiative Complete

1. All 77 contracts centralized, searchable, and AI-ready (current executed versions only)
2. Every customer has a verified MSA summary — including logo, marketing, and reference restrictions
3. Every active SOW has a complete inventory record with exceptions flagged separately
4. Weekly AI-assisted exec slide operational and delivering business intelligence
5. Invoice details linked to active SOWs with documented variance explanations (contracted, deployed, billed)
6. Product Naming and Pricing/Packaging strategic initiatives have a trusted baseline dataset
7. CLM evaluation criteria defined from discovered metadata requirements (W6 trigger)
8. Repository functions as an **AI-powered contract intelligence platform** — not a passive document library

---

*v2 — Merged executive and operational plan. Living document; refined weekly as workstreams progress.*
