# Renewal Data — Cleanup & Enrichment Package

**Owner:** Jason Yuhas, VP of Commercial Operations
**Purpose:** Fix the renewal dataset (Aug 2026 – Aug 2027) and stage it for enrichment once Google Drive, Gong, and Atlassian are connected.
**Source of truth:** Salesforce (read-only via MCP). Writes require Data Loader or a write-enabled connection.
**Last Updated:** 2026-08-13

> **Scope note:** 128 open renewal records across 87 accounts. Every record currently has `Amount = $0` and `Probability = 25%`, 65 lack `NextStep`, and ~30 have impossible future `LastActivityDate` values. This package corrects structure and scoring; dollar values and terms require the enrichment sources below.

---

## 1. Data-quality defects and fixes

| # | Defect | Records affected | Fix | Applied by |
|---|--------|------------------|-----|-----------|
| D1 | `Amount = $0` on all renewals | 128 | Backfill ARR from executed contract / prior order value | Finance export or contract repo → Data Loader |
| D2 | Flat `Probability = 25%` | 128 | Replace with **Renewal Health Score** (Section 3) | RevOps (Data Loader) |
| D3 | Missing `NextStep` | 65 | Apply templated next step per tier (Section 4) | CS/Sales owners |
| D4 | Future-dated `LastActivityDate` | ~30 | Correct to true last-touch date | RevOps (Section 2) |
| D5 | 128 product-level records, no account rollup | 87 accounts | Add parent-account renewal play (Section 5) | RevOps |
| D6 | No contract terms (TFC, auto-renewal, notice) | ~all | Enrich from Drive/contract repo (Section 6) | Contract Intelligence W2–W4 |
| D7 | Utilization not linked to renewal | ~all | Attach adoption scorecard from Evolve/Looker | CS Analytics |

---

## 2. Cleanup list generators (reproducible SOQL)

Run these read-only queries to regenerate exact cleanup lists at any time. They avoid hand-transcription error.

**D4 — Future-dated activity (data corruption):**
```sql
SELECT Id, Account.Name, Name, LastActivityDate, Owner.Name
FROM Opportunity
WHERE IsClosed = false
  AND (Type LIKE '%Renew%' OR Name LIKE '%Renew%')
  AND LastActivityDate > TODAY
ORDER BY LastActivityDate DESC
```

**D3 — Renewals missing a next step (planning gap):**
```sql
SELECT Id, Account.Name, Name, CloseDate, Owner.Name
FROM Opportunity
WHERE IsClosed = false
  AND (Type LIKE '%Renew%' OR Name LIKE '%Renew%')
  AND CloseDate >= 2026-08-13 AND CloseDate <= 2027-08-13
  AND NextStep = null
ORDER BY CloseDate ASC
```

**D1/D2 — Renewals with no economics or default probability:**
```sql
SELECT Id, Account.Name, Name, CloseDate, Amount, Probability
FROM Opportunity
WHERE IsClosed = false
  AND (Type LIKE '%Renew%' OR Name LIKE '%Renew%')
  AND CloseDate >= 2026-08-13 AND CloseDate <= 2027-08-13
  AND (Amount = 0 OR Amount = null OR Probability = 25)
ORDER BY CloseDate ASC
```

> Known future-dated accounts already identified (correct these first): Broward Health, Mount Sinai, Community Medical Centers, Baystate, Scripps, Sturdy Memorial, UMass HealthAlliance, Eskenazi, AnMed, Centinela, Stony Brook, Texas Children's, United Regional, Inova, Cambridge, UCSF, Virginia Mason Franciscan, University of Illinois Hospital, Providence Everett, Providence South Division, UCLA, Banner, Cedars-Sinai, Licking Memorial, Mayo Jacksonville, Trinity Health New England.

---

## 3. Renewal Health Score (replaces flat 25%)

A transparent 0–100 score. Until enrichment lands, compute the **provisional** score from available Salesforce signals; add the enriched factors as systems connect.

| Factor | Weight | Provisional source (SF today) | Enriched source |
|--------|--------|-------------------------------|-----------------|
| Relationship / champion strength | 25 | # distinct contacts on activities | Gong call breadth + outcomes |
| Engagement recency | 15 | valid `LastActivityDate` (exclude future dates) | Gong + Calendar |
| Utilization vs. contract | 20 | — (unavailable) | Evolve/Looker adoption trend |
| QBR/EBR completed in last 12 mo | 10 | Event subject scan | Calendar + Confluence |
| Executive sponsor identified | 10 | Contact roles | Drive/CRM people map |
| Contract risk (TFC / short notice / auto-renew) | 10 | — (unavailable) | Contract repo (W2–W4) |
| Commercial trend (price, billing variance) | 10 | — (unavailable) | Invoice reconciliation (W5) |

**Provisional banding (what I can compute now):**
- **Green (renew + expand):** multi-threaded, recent valid activity, QBR/EBR done
- **Yellow (stabilize):** single-threaded or stale activity, no recent review
- **Red (at risk):** explicit churn/offboarding/decline signal, or no owner/next step

Provisional example classifications from current evidence:
- **Red:** Grays Harbor (end of contract), Marshall (offboarding), United Regional (NOT_INTERESTED/GATEKEEPER)
- **Yellow:** UC Davis (stale steps), UC San Diego (transition), Sturdy (staffing), OneBrooklyn (CSM change)
- **Green-leaning:** Norton, Johns Hopkins, HCA St. David's (multi-threaded, active) — pending utilization confirmation

---

## 4. Next-step templates (fills D3)

| Tier (days to renewal) | Templated next step |
|------------------------|---------------------|
| 0–30 | Confirm renewal disposition + notice status; secure exec sponsor; start paper |
| 31–90 | Schedule EBR; deliver value/outcomes review; verify auto-renewal + TFC |
| 91–180 | Build people map (6 roles); adoption scorecard; expansion hypothesis |
| 181–365 | Verify contract terms; baseline utilization; assign owner |

---

## 5. Consolidated account model (fixes D5)

Replace 128 fragmented product opportunities with **87 parent-account renewal plays**. Each parent play carries: earliest renewal, product/record count, health tier, owner, exec sponsor, EBR date, and one expansion thesis. The near-term 22 (≤90 days) are fully scoped in the renewal analysis already delivered; the remaining 65 follow the same template at 180 days out.

---

## 6. Enrichment map — what unlocks when you connect each system

| System | Status | Fields it fills | Blind spot it closes |
|--------|--------|-----------------|----------------------|
| **Google Drive** | ⛔ needs auth | Executed MSA/SOW terms: renewal date, auto-renewal, **TFC**, notice window, special terms, price, referenced future pricing; QBR/EBR decks | The #1 gap — no contract terms in CRM today |
| **Gong** | ⛔ errored | Real call outcomes, champion strength, sentiment, next steps | 198/200 call outcomes currently blank |
| **Atlassian (Confluence/Jira)** | ⛔ needs auth | Account plans, EBR notes, escalations, product commitments | QBR/EBR content and open issues |
| **Evolve / Looker** | export | Adoption trend (contracted vs. deployed vs. used), underused programs | Utilization is anecdotal today |
| **Invoices (W5)** | pending | Billed vs. contracted variance, price increases | Revenue leakage on renewal |
| **Salesforce** | ✅ live | Dates, owners, structure | (source of truth) |

---

## 7. Execution order

1. **You:** connect Google Drive, Gong, Atlassian (Desktop → Settings → Tools & MCP → Connect; or Cloud Agent → Secrets).
2. **Now (no auth):** cleanup lists (Section 2), health-score model (Section 3), next-step templates (Section 4), consolidated model (Section 5).
3. **After auth:** enrich terms + utilization + champion scores; recompute health scores with full weighting.
4. **RevOps/Finance:** load corrected `Amount`, `Probability`, `NextStep`, `LastActivityDate` via Data Loader (MCP is read-only).
5. **Weekly:** renewal win rooms for multi-entity systems (HCA, UMass, Providence, Norton, Johns Hopkins).

---

*Living document. Section 6 statuses update automatically as each MCP connection comes online.*
