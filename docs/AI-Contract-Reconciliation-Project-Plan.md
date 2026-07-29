# AI Contract Reconciliation Initiative — Project Plan

**Project Lead:** Jason  
**Status:** Immediate focus (post sales leadership, territories, and compensation finalization)  
**Last Updated:** 2026-07-29

---

## Executive Summary

This initiative is more than a contract cleanup effort. It establishes a foundational capability for AI RevOps maturity and will become a strategic asset for **Sales, Finance, Legal, Customer Success, and Product**.

The end goal is an **AI-powered contract intelligence repository** — not simply a document library — that enables:

- Strategic account planning
- Renewal management
- Pricing governance
- Expansion identification
- Customer insights and forecasting
- Future AI automation

**Guiding principle:** AI accelerates the work; all outputs are **trust, but verify**. The objective is strategic account planning — not legal interpretation.

---

## Sequencing Overview

```mermaid
gantt
    title AI Contract Reconciliation — Phased Delivery
    dateFormat  YYYY-MM-DD
    section Phase 1 — Foundation
    Weekly progress automation           :p1a, 2026-07-29, 7d
    Contract repository (77 contracts) :p1b, 2026-07-29, 21d
    MSA summaries                        :p1c, after p1b, 21d
    Active SOW inventory                 :p1d, after p1b, 21d
    section Phase 2 — Automation
    Renewal calendar & workflow eval     :p2a, after p1c, 14d
    Cross-functional automation design   :p2b, after p2a, 14d
    section Phase 3 — Billing Integration
    Invoice-to-SOW linkage (Chris)       :p3a, after p2b, 21d
```

| Phase | Focus | Gate to Proceed |
|-------|-------|-----------------|
| **Phase 1** | Foundational data — repository, MSA summaries, SOW inventory | Clean, trusted, searchable dataset complete |
| **Phase 2** | AI-driven automation evaluation (renewals, notifications, orchestration) | Phase 1 complete; cross-functional teams engaged |
| **Phase 3** | Invoice integration — contracted vs. deployed vs. billed | Phase 2 automation scope defined |

> **Important:** Cross-functional automation discussions begin **after** Phase 1 foundational work is complete — not before. Establish a clean, trusted data set first, then automate from there.

---

## Phase 1 — Foundational Contract Intelligence

### 1.1 Weekly Progress Reporting (Ongoing)

**Owner:** Jason (with AI automation)

Leverage AI to automate a weekly update to the project team and SLT. Each update must include:

| Section | Content |
|---------|---------|
| **Overall progress** | % complete against Phase 1 deliverables |
| **Key accomplishments** | What was completed since last update |
| **Risks, blockers, and decisions needed** | Items requiring leadership or cross-functional input |
| **Remaining work** | Open tasks with projected completion timeline |

**Deliverable:** Recurring weekly status report (automated draft + human review before send)

---

### 1.2 Contract Repository — 77 Contracts

**Scope:** Every customer, organized by parent organization

| Requirement | Detail |
|-------------|--------|
| Centralization | All executed agreements in a single repository |
| Storage & naming | Establish and document long-term storage location and naming convention |
| Searchability | Every document searchable and AI-ready |

**Deliverables:**
- [ ] Central contract repository populated with all 77 executed agreements
- [ ] Parent-organization hierarchy documented
- [ ] Storage location and naming convention documented (runbook)
- [ ] Documents indexed for search and AI ingestion

**Success criteria:** Any team member can locate any customer agreement by parent org, entity, or contract type within minutes.

---

### 1.3 MSA Summary — Per Customer

**Tooling:** Cursor / AI-assisted extraction with human verification

Generate a standardized summary for each customer:

| Field | Purpose |
|-------|---------|
| MSA title | Identification |
| Parent organization and covered entities | Account hierarchy |
| MSA extends to child accounts/affiliates? | Expansion opportunity identification |
| Signature date | Contract timeline |
| Customer signer | Relationship context |
| Order of precedence | Conflict resolution across agreements |
| Contract term | Duration and obligations |
| Renewal date and renewal language | Renewal planning (including agreements that remain active while an SOW is active) |
| Notable commercial, legal, or operational provisions | Account strategy impact |

**Deliverables:**
- [ ] Standardized MSA summary template
- [ ] MSA summary for each customer in the repository
- [ ] Flagged items requiring Legal or Finance review

**Success criteria:** Sales and CS can use MSA summaries for strategic account planning without opening source PDFs.

---

### 1.4 Active SOW Inventory — Per Active SOW

For every active Statement of Work, capture:

| Field | Purpose |
|-------|---------|
| Product names / modules purchased | Entitlement clarity |
| Programs, workflows, and use cases deployed | Deployment vs. contract alignment |
| Scripts / campaign details (where applicable) | Operational context |
| Contracted volumes and utilization commitments | Usage governance |
| Contracted pricing | Pricing baseline |
| Referenced future pricing | Renewal / expansion forecasting |
| Go-live date | Timeline context |
| Termination-for-convenience provisions | Risk and renewal planning |
| Auto-renewal terms and notice requirements | Renewal calendar inputs |
| Non-standard amendments (email, side letters, etc.) | **Flag separately** — exceptions and commercial changes outside standard amendments |

**Deliverables:**
- [ ] Standardized SOW inventory template
- [ ] Active SOW record for each in-scope SOW
- [ ] Separate exception/amendment log for non-standard changes

**Success criteria:** Complete view of what is contracted and deployed for every active customer engagement.

---

## Phase 2 — AI-Driven Automation Evaluation

**Prerequisite:** Phase 1 complete (clean, trusted dataset)

**Owner:** Jason (with cross-functional teams brought in by leadership)

Once the initial repository and summaries are complete, evaluate where AI-driven automations add value:

| Automation Area | Description |
|-----------------|-------------|
| **Renewal management** | Rolling 12-month renewal calendar |
| **Notifications** | Proactive alerts for renewal windows, notice periods, and term expirations |
| **Workflow orchestration** | Cross-team handoffs for renewal prep, Legal review, and Finance alignment |

**Deliverables:**
- [ ] Automation opportunity assessment (prioritized)
- [ ] Rolling 12-month renewal calendar (initial version)
- [ ] Recommended automation roadmap with owners
- [ ] Cross-functional working session outcomes (Sales, Finance, Legal, CS, Product)

**Success criteria:** Leadership-approved automation roadmap with clear ROI and ownership.

---

## Phase 3 — Invoice Integration

**Owner:** Chris  
**Prerequisite:** Phase 2 automation scope defined

Connect the latest invoice details to each active SOW to achieve a complete view of:

| Dimension | Question Answered |
|-----------|-------------------|
| **Contracted** | What did the customer agree to? |
| **Deployed** | What is live in production? |
| **Billed** | What is currently being invoiced? |

**Deliverables:**
- [ ] Invoice-to-SOW mapping for all active accounts
- [ ] Discrepancy report (contracted vs. deployed vs. billed)
- [ ] Integrated account view in the contract intelligence repository

**Success criteria:** Single source of truth linking contract terms, deployment status, and billing for every active customer.

---

## Stakeholders & Roles

| Role | Name | Responsibility |
|------|------|----------------|
| **Project Lead** | Jason | Overall delivery, weekly reporting, Phase 1 & 2 |
| **Billing Integration** | Chris | Phase 3 — invoice-to-SOW linkage |
| **Executive Sponsor** | — | Priority setting, cross-functional escalation |
| **SLT** | — | Weekly progress visibility |
| **Sales, Finance, Legal, CS, Product** | — | Phase 2 cross-functional input; trust-but-verify on outputs |

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Incomplete or missing contracts | Gaps in repository | Audit against CRM/account list; escalate missing docs to Legal |
| AI extraction errors | Incorrect summaries | Trust-but-verify workflow; Legal/Finance review for flagged items |
| Non-standard amendments overlooked | Commercial surprises | Dedicated exception log; separate flagging in SOW inventory |
| Scope creep into automation before data is clean | Rework, low trust | Enforce Phase 1 gate before Phase 2 cross-functional sessions |
| Resource constraints on Jason | Timeline slip | AI acceleration for extraction; clear prioritization of 77 contracts |

---

## Key Decisions Needed

| Decision | Owner | Timing |
|----------|-------|--------|
| Long-term storage location and naming convention | Jason + IT/Legal | Phase 1 kickoff |
| MSA/SOW summary template approval | Jason + Legal | Before bulk extraction |
| Exception/amendment handling process | Jason + Legal | Phase 1 |
| Automation priority ranking | Leadership + Jason | Phase 2 kickoff |
| Invoice data source and mapping rules | Chris + Finance | Phase 3 kickoff |

---

## Definition of Done — Initiative Complete

The initiative is complete when:

1. All 77 contracts are centralized, searchable, and AI-ready
2. Every customer has a verified MSA summary
3. Every active SOW has a complete inventory record with exceptions flagged
4. Weekly AI-assisted progress reporting is operational
5. A rolling 12-month renewal calendar and automation roadmap are approved
6. Invoice details are linked to active SOWs (Phase 3)
7. The repository functions as an **AI-powered contract intelligence platform** — not a passive document library

---

## Appendix — Document Templates (To Be Created)

- [ ] Contract naming convention runbook
- [ ] MSA summary template
- [ ] Active SOW inventory template
- [ ] Non-standard amendment / exception log
- [ ] Weekly progress report template
- [ ] Renewal calendar template
