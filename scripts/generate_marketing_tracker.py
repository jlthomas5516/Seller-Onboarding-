#!/usr/bin/env python3
"""Generate Q3-Q4 2026 marketing plan xlsx tracker from plan context."""

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

BRAND = {
    "teal": "00B4A4",
    "violet": "5B4FB5",
    "chartreuse": "B5CC2E",
    "amber": "E8A020",
    "anchor": "2D2660",
    "lavender": "F2F1F9",
    "white": "FFFFFF",
    "light_violet": "E9E7F5",
}

thin = Side(style="thin", color="E0DCF0")
border = Border(left=thin, right=thin, top=thin, bottom=thin)
header_fill = PatternFill("solid", fgColor=BRAND["anchor"])
header_font = Font(name="Calibri", bold=True, color=BRAND["white"], size=11)
subheader_fill = PatternFill("solid", fgColor=BRAND["violet"])
subheader_font = Font(name="Calibri", bold=True, color=BRAND["white"], size=10)
section_fill = PatternFill("solid", fgColor=BRAND["lavender"])
section_font = Font(name="Calibri", bold=True, color=BRAND["anchor"], size=10)
body_font = Font(name="Calibri", size=10, color=BRAND["anchor"])
wrap = Alignment(wrap_text=True, vertical="top")
center = Alignment(horizontal="center", vertical="center", wrap_text=True)

STATUS_OPTIONS = "Not Started,In Progress,Blocked,Complete,Cancelled"
PILLARS = "Pipeline Recovery,Product Narrative,Customer Proof,Field & Community"


def style_header_row(ws, row, cols, fill=header_fill, font=header_font):
    for c in range(1, cols + 1):
        cell = ws.cell(row=row, column=c)
        cell.fill = fill
        cell.font = font
        cell.alignment = center
        cell.border = border


def write_table(ws, start_row, headers, rows, col_widths=None):
    style_header_row(ws, start_row, len(headers))
    for i, h in enumerate(headers, 1):
        ws.cell(row=start_row, column=i, value=h).border = border
    for r_idx, row in enumerate(rows, start_row + 1):
        for c_idx, val in enumerate(row, 1):
            cell = ws.cell(row=r_idx, column=c_idx, value=val)
            cell.font = body_font
            cell.alignment = wrap
            cell.border = border
    if col_widths:
        for i, w in enumerate(col_widths, 1):
            ws.column_dimensions[get_column_letter(i)].width = w
    return start_row + len(rows) + 2


def build_summary(wb):
    ws = wb.active
    ws.title = "Dashboard"
    ws["A1"] = "CipherHealth Marketing Plan Tracker — Q3-Q4 2026"
    ws["A1"].font = Font(name="Calibri", bold=True, size=16, color=BRAND["anchor"])
    ws.merge_cells("A1:H1")

    ws["A3"] = "Last updated"
    ws["B3"] = "2026-08-06"
    ws["A4"] = "Marketing lead"
    ws["B4"] = "[Assign owner]"
    ws["A5"] = "Plan status"
    ws["B5"] = "Draft — pending 6 leadership decisions"

    metrics = [
        ("Metric", "Target", "Actual / Plan", "Attainment", "Notes"),
        ("Q3 Marketing Pipeline", "$2.2M", "$240K", "11%", "Critical gap — Sept/Oct recovery plan targets ~$1.4M new pipe"),
        ("Q4 Marketing Pipeline", "$1.6M", "TBD", "—", "Depends on NGPX + CCI moment"),
        ("Q3-Q4 Ad Budget (planned)", "$124K ($31K/mo)", "$124K", "100% allocated", "Leadership decision: approve $40-45K/mo or accept lower recovery"),
        ("Sept/Oct New Pipe Target", "~$1.4M", "—", "—", "Even at 100% hit, Q3 closes ~73% ($1.6M of $2.2M)"),
    ]
    write_table(ws, 7, metrics[0], metrics[1:], [22, 14, 14, 12, 48])

    ws["A14"] = "Strategic Pillars (tag every row)"
    ws["A14"].font = section_font
    ws["A14"].fill = section_fill
    ws.merge_cells("A14:H14")
    pillars = [
        "1. Pipeline Recovery — close Q3 gap, set up Q4/November pipeline",
        "2. Product Narrative — hero webinar + CCI reveal positioning",
        "3. Customer Proof — panel webinars, case studies, reference selling",
        "4. Field & Community — CX Exchange, NGPX, Beryl regional chapters",
    ]
    for i, p in enumerate(pillars, 15):
        ws[f"A{i}"] = p
        ws[f"A{i}"].font = body_font
        ws.merge_cells(f"A{i}:H{i}")

    ws.column_dimensions["A"].width = 22
    ws.column_dimensions["B"].width = 14


def build_weekly_calendar(wb, sheet_name, weeks):
    ws = wb.create_sheet(sheet_name)
    headers = [
        "Week Of",
        "Category",
        "Pillar",
        "Activity / Deliverable",
        "Owner",
        "Status",
        "Pipeline $ Target",
        "Notes / Dependencies",
    ]
    write_table(ws, 1, headers, weeks, [12, 14, 18, 42, 14, 14, 14, 36])


def build_social(wb):
    ws = wb.create_sheet("Social Calendar")
    headers = [
        "Week Of",
        "Day",
        "Owner",
        "Pillar",
        "Channel",
        "Topic / Hook",
        "Asset Needed",
        "Status",
        "Publish Date",
    ]
    rows = [
        ("2026-09-01", "Mon", "Zach", "Product Narrative", "LinkedIn", "AI infrastructure positioning teaser (pending Aug 15 lock)", "Static + quote card", "Not Started", "2026-09-02"),
        ("2026-09-01", "Tue", "Jen", "Pipeline Recovery", "LinkedIn", "Sept 24 webinar save-the-date", "Webinar graphic", "Not Started", "2026-09-03"),
        ("2026-09-01", "Wed", "Joy", "Field & Community", "LinkedIn", "Beryl regional chapter preview", "Event photo / logo", "Not Started", "2026-09-04"),
        ("2026-09-01", "Thu", "Christy", "Customer Proof", "LinkedIn", "Customer outcome stat (UM Health or selected customer)", "Stat card", "Not Started", "2026-09-05"),
        ("2026-09-01", "Fri", "Exec (rotate)", "Pipeline Recovery", "LinkedIn", "Thought leadership — care coordination at scale", "Exec headshot", "Not Started", "2026-09-06"),
        ("2026-09-08", "Mon", "Zach", "Product Narrative", "LinkedIn + X", "Product + customer co-presenter announcement", "Speaker bios", "Not Started", "2026-09-09"),
        ("2026-09-08", "Tue", "Jen", "Pipeline Recovery", "LinkedIn", "Webinar registration push #1", "Registration link", "Not Started", "2026-09-10"),
        ("2026-09-08", "Wed", "Joy", "Field & Community", "LinkedIn", "CX Exchange East — confirm or pivot message", "Event badge", "Blocked", "2026-09-11"),
        ("2026-09-08", "Thu", "Christy", "Customer Proof", "LinkedIn", "Customer quote / mini case", "Approved quote", "Not Started", "2026-09-12"),
        ("2026-09-08", "Fri", "Exec (rotate)", "Product Narrative", "LinkedIn", "Why now: operational AI in health systems", "Blog link", "Not Started", "2026-09-13"),
        ("2026-09-15", "Mon", "Zach", "Product Narrative", "LinkedIn", "Webinar agenda reveal — 3 takeaways", "Agenda graphic", "Not Started", "2026-09-16"),
        ("2026-09-15", "Tue", "Jen", "Pipeline Recovery", "LinkedIn + Email", "Webinar registration push #2 (48hr urgency)", "Countdown creative", "Not Started", "2026-09-17"),
        ("2026-09-15", "Wed", "Joy", "Field & Community", "LinkedIn", "Beryl chapter meeting recap or promo", "Chapter logo", "Not Started", "2026-09-18"),
        ("2026-09-15", "Thu", "Christy", "Customer Proof", "LinkedIn", "Speaker spotlight — customer executive", "Headshot", "Not Started", "2026-09-19"),
        ("2026-09-15", "Fri", "Exec (rotate)", "Pipeline Recovery", "LinkedIn", "Pipeline / market POV", "—", "Not Started", "2026-09-20"),
        ("2026-09-22", "Mon", "Zach", "Product Narrative", "LinkedIn", "24-hour webinar countdown", "Live badge", "Not Started", "2026-09-23"),
        ("2026-09-22", "Tue", "Jen", "Pipeline Recovery", "LinkedIn + Email", "Final registration push", "Reminder email", "Not Started", "2026-09-23"),
        ("2026-09-22", "Wed", "Joy", "Field & Community", "LinkedIn", "Live-tweet/webinar day-of thread", "Hashtag set", "Not Started", "2026-09-24"),
        ("2026-09-22", "Thu", "Christy", "Customer Proof", "LinkedIn", "Post-webinar thank you + recording CTA", "Recording link", "Not Started", "2026-09-25"),
        ("2026-09-22", "Fri", "Exec (rotate)", "Customer Proof", "LinkedIn", "Key takeaway from Sept 24 session", "Clip / quote", "Not Started", "2026-09-26"),
    ]
    write_table(ws, 1, headers, rows, [12, 8, 14, 18, 12, 38, 20, 14, 12])


def build_webinars(wb):
    ws = wb.create_sheet("Webinars")
    headers = [
        "Date",
        "Title (working)",
        "Type",
        "Speakers",
        "Customer",
        "PM Owner",
        "Mktg Owner",
        "Reg Target",
        "Pipe Target",
        "Producer",
        "Status",
        "Promo Start",
        "Notes",
    ]
    rows = [
        (
            "2026-09-24",
            "Hero Product Webinar — Care Coordination / AI Infrastructure (TBD positioning)",
            "Hero launch",
            "Zach + Product + Customer executive",
            "TBD — UM Health / Penn / Norton (Henry Ford backup)",
            "[Product Marketing]",
            "Jen",
            "300",
            "$500K",
            "Contractor $8-12K (pending approval)",
            "Planning",
            "2026-09-03",
            "Lock customer by Aug 15; positioning language by Aug 15",
        ),
        (
            "2026-10-22",
            "Customer Panel — Operational Outcomes at Scale",
            "Customer proof",
            "2-3 customers + moderator",
            "Panel TBD",
            "[Product Marketing]",
            "Jen",
            "250",
            "$400K",
            "Same contractor",
            "Planning",
            "2026-10-01",
            "Recruit panelists from Sept 24 registrants + CS references",
        ),
        (
            "2026-11-12",
            "CCI Reveal — Product Moment",
            "Feature launch",
            "Product + Zach",
            "N/A",
            "[Product Marketing]",
            "Jen",
            "350",
            "$500K",
            "Internal or contractor",
            "Not Started",
            "2026-10-20",
            "Anchor Q4 pipeline; coordinate with product GA timing",
        ),
    ]
    write_table(ws, 1, headers, rows, [12, 36, 14, 24, 18, 16, 12, 10, 12, 18, 12, 12, 32])


def build_field_events(wb):
    ws = wb.create_sheet("Field Events")
    headers = [
        "Date",
        "Event",
        "Type",
        "Location",
        "Owner",
        "Budget",
        "Pipe Target",
        "Status",
        "Notes",
    ]
    rows = [
        ("2026-09 TBD", "Beryl Institute Regional Chapter #1", "Regional field", "TBD — Joy selects", "Joy", "$2-4K", "$75K", "Planning", "Layer local field events under ElevatePX national Q1 narrative"),
        ("2026-10 TBD", "Beryl Institute Regional Chapter #2", "Regional field", "TBD — Joy selects", "Joy", "$2-4K", "$75K", "Planning", "Pick chapters with active member hospitals in ICP"),
        ("2026-10-12", "CX Exchange East", "Conference", "East (TBD city)", "Joy + AE team", "$8-15K", "$200K", "Under consideration", "CONFIRM by Aug 15 — recommend yes if 3+ target accounts attending"),
        ("2026-12-02", "NGPX", "Conference / Sponsorship", "Palm Springs", "Jen + Events", "Confirmed sponsorship", "$450K", "Confirmed", "Anchor Q4 pipeline; book meetings by Nov 1"),
    ]
    write_table(ws, 1, headers, rows, [12, 28, 14, 18, 14, 12, 12, 16, 36])


def build_pipeline(wb):
    ws = wb.create_sheet("Pipeline Targets")
    headers = ["Month", "Source", "Target ($)", "Actual ($)", "Attainment %", "Owner", "Notes"]
    rows = [
        ("2026-09", "Paid digital", "$180K", "", "", "Jen", "Requires $40-45K/mo budget approval vs $31K plan"),
        ("2026-09", "Webinar (Sept 24)", "$500K", "", "", "Jen", "Hero webinar — primary September pipe driver"),
        ("2026-09", "Field / Beryl regional", "$75K", "", "", "Joy", "Chapter meeting #1"),
        ("2026-09", "Content / inbound", "$100K", "", "", "Christy", "Gated assets + nurture"),
        ("2026-09", "TOTAL", "$855K", "$240K YTD Q3", "11% Q3 YTD", "Marketing", "Sept alone won't close full Q3 gap"),
        ("2026-10", "Paid digital", "$180K", "", "", "Jen", ""),
        ("2026-10", "CX Exchange East", "$200K", "", "", "Joy", "Contingent on Aug 15 confirmation"),
        ("2026-10", "Webinar (Oct 22 panel)", "$400K", "", "", "Jen", ""),
        ("2026-10", "Field / Beryl regional", "$75K", "", "", "Joy", "Chapter meeting #2"),
        ("2026-10", "Content / inbound", "$100K", "", "", "Christy", ""),
        ("2026-10", "TOTAL", "$955K", "", "", "Marketing", "Combined Sept+Oct ~$1.4M new pipe target"),
        ("2026-11", "Paid digital", "$180K", "", "", "Jen", ""),
        ("2026-11", "Webinar (Nov 12 CCI)", "$500K", "", "", "Jen + PM", "Product moment"),
        ("2026-11", "Field / retention", "$150K", "", "", "CS + Marketing", "Customer expansion campaigns"),
        ("2026-11", "TOTAL", "$830K", "", "", "Marketing", ""),
        ("2026-12", "NGPX", "$450K", "", "", "Jen", "Confirmed sponsorship"),
        ("2026-12", "Paid digital", "$180K", "", "", "Jen", ""),
        ("2026-12", "Retention / year-end", "$200K", "", "", "Christy", ""),
        ("2026-12", "TOTAL", "$830K", "", "", "Marketing", "Q4 attainment decided here"),
    ]
    write_table(ws, 1, headers, rows, [12, 22, 12, 12, 12, 12, 40])


def build_decisions(wb):
    ws = wb.create_sheet("Open Decisions")
    headers = ["#", "Decision", "Options", "Owner", "Due Date", "Status", "Impact if delayed"]
    rows = [
        (1, "Lock positioning language", "AI infrastructure vs care coordination infrastructure", "Executive + PM", "2026-08-15", "Open", "Blocks all Sept 24 creative, ads, and webinar title"),
        (2, "Confirm CX Exchange East attendance", "Attend vs skip", "Joy + Jen", "2026-08-15", "Open", "$200K Oct pipe at risk"),
        (3, "Approve ad budget increase", "$40-45K/mo vs $31K plan", "Chris (CFO)", "2026-08-15", "Open", "Lower paid pipe recovery in Q3-Q4"),
        (4, "Approve webinar producer contractor", "$8-12K for Sept 24 + Oct 22", "Jen Thomas", "2026-08-15", "Open", "Production quality / on-time delivery risk"),
        (5, "Select Sept 24 customer speaker", "UM Health / Penn / Norton (Henry Ford backup)", "CS + Zach", "2026-08-15", "Open", "Cannot finalize promo without named customer"),
        (6, "Select two Beryl regional chapters", "Joy to recommend based on ICP density", "Joy", "2026-08-22", "Open", "Field event logistics and local pipe"),
    ]
    write_table(ws, 1, headers, rows, [4, 32, 28, 14, 12, 12, 36])


def build_measurement(wb):
    ws = wb.create_sheet("Measurement")
    headers = ["Cadence", "Metric", "Owner", "Distribution", "Next Due"]
    rows = [
        ("Weekly", "Pipeline created by source vs target", "Jen", "Marketing standup + SLT slack", "Every Monday"),
        ("Weekly", "Webinar reg / attendance / pipe", "Jen", "Marketing standup", "Every Monday"),
        ("Weekly", "Paid media spend vs CPA", "Jen", "Marketing + Finance", "Every Friday"),
        ("Monthly", "Marketing-sourced pipeline attainment", "Jen", "CSO + CFO", "First business day"),
        ("Monthly", "Content / social engagement vs plan", "Christy", "Marketing team", "First business day"),
        ("Monthly", "Event ROI (meetings held, pipe)", "Joy", "Marketing + Sales", "Within 5 days post-event"),
        ("Quarterly", "Q3/Q4 pipeline vs annual plan", "Jen", "Board / exec team", "Quarter close + 10 days"),
    ]
    write_table(ws, 1, headers, rows, [12, 32, 12, 24, 16])


def build_q4_outline(wb):
    ws = wb.create_sheet("Q4 Outline")
    headers = ["Week Of", "Category", "Activity", "Owner", "Status", "Pipe Target", "Notes"]
    rows = [
        ("2026-11-03", "Lead Gen", "Nov paid campaign launch — CCI teaser", "Jen", "Not Started", "$180K", ""),
        ("2026-11-03", "Content", "CCI reveal content sprint begins", "Christy + PM", "Not Started", "", ""),
        ("2026-11-10", "Feature Launch", "Nov 12 CCI Reveal webinar", "Jen + PM", "Planning", "$500K", "Anchor Q4 product moment"),
        ("2026-11-17", "Retention", "Customer expansion email series", "Christy", "Not Started", "$75K", ""),
        ("2026-11-24", "Lead Gen", "NGPX pre-book meeting campaign", "Jen + Joy", "Not Started", "$100K", "Target accounts only"),
        ("2026-12-01", "Conference", "NGPX Dec 2-4 Palm Springs", "Jen + Events", "Confirmed", "$450K", "Confirmed sponsorship"),
        ("2026-12-08", "Retention", "Year-end customer thank-you + renewal touch", "Christy + CS", "Not Started", "$100K", ""),
        ("2026-12-15", "Lead Gen", "Q1 2027 pipeline seeding — ElevatePX / Beryl", "Joy", "Not Started", "$50K", "Bridge to national ElevatePX Q1"),
    ]
    write_table(ws, 1, headers, rows, [12, 16, 36, 14, 14, 12, 32])


def main():
    wb = Workbook()
    build_summary(wb)

    sept_weeks = [
        ("2026-09-01", "Lead Gen", "Pipeline Recovery", "Paid search + LinkedIn campaign launch (pending budget approval)", "Jen", "Not Started", "$60K", "Creative blocked on positioning decision"),
        ("2026-09-01", "Content", "Product Narrative", "Webinar landing page + save-the-date email #1", "Christy", "Not Started", "$50K", "Needs customer name by Aug 15"),
        ("2026-09-01", "PR", "Product Narrative", "Optional: trade press outreach for Sept 24 webinar", "Christy", "Not Started", "$25K", "Only if positioning locked early"),
        ("2026-09-08", "Lead Gen", "Pipeline Recovery", "Webinar promo email #2 + paid retargeting", "Jen", "Not Started", "$80K", ""),
        ("2026-09-08", "Content", "Customer Proof", "Customer proof asset — stat card + quote approval", "Christy", "Not Started", "$25K", "UM Health / Penn / Norton"),
        ("2026-09-08", "Field", "Field & Community", "Beryl regional chapter #1 — logistics + invite list", "Joy", "Planning", "$75K", "Chapter TBD by Joy"),
        ("2026-09-15", "Lead Gen", "Pipeline Recovery", "Webinar promo email #3 + 1:1 AE outreach to target accounts", "Jen + AEs", "Not Started", "$120K", "AE team: top 50 accounts"),
        ("2026-09-15", "Content", "Product Narrative", "Speaker prep + dry run (Zach + customer + PM)", "Jen + PM", "Not Started", "", "Contractor runs production"),
        ("2026-09-15", "Retention", "Customer Proof", "CS reference outreach for Oct 22 panel", "CS", "Not Started", "", ""),
        ("2026-09-22", "Lead Gen", "Pipeline Recovery", "Final reg push + day-of reminders", "Jen", "Not Started", "$100K", ""),
        ("2026-09-24", "Lead Gen", "Product Narrative", "HERO WEBINAR — Zach + Product + Customer", "Jen + PM", "Planning", "$500K", "Primary September pipe event"),
        ("2026-09-22", "Content", "Customer Proof", "Post-webinar nurture sequence + recording gated asset", "Christy", "Not Started", "$50K", "Launch Sept 25"),
    ]
    build_weekly_calendar(wb, "September 2026", sept_weeks)

    oct_weeks = [
        ("2026-10-06", "Lead Gen", "Pipeline Recovery", "October paid campaign — customer proof angle", "Jen", "Not Started", "$60K", ""),
        ("2026-10-06", "Content", "Customer Proof", "Oct 22 panel landing page + speaker bios", "Christy", "Not Started", "$40K", ""),
        ("2026-10-06", "Field", "Field & Community", "CX Exchange East prep — meetings, booth, materials", "Joy", "Blocked", "$200K", "CONFIRM attendance by Aug 15"),
        ("2026-10-12", "Conference", "Field & Community", "CX Exchange East (Oct 12-13)", "Joy + AEs", "Under consideration", "$200K", "2-day event"),
        ("2026-10-13", "Field", "Field & Community", "Beryl regional chapter #2", "Joy", "Planning", "$75K", "Chapter TBD"),
        ("2026-10-20", "Lead Gen", "Customer Proof", "Oct 22 panel promo blitz", "Jen", "Not Started", "$80K", ""),
        ("2026-10-22", "Lead Gen", "Customer Proof", "CUSTOMER PANEL WEBINAR", "Jen", "Planning", "$400K", "2-3 customer speakers"),
        ("2026-10-27", "Content", "Pipeline Recovery", "Q4 pipeline content — CCI teaser", "Christy + PM", "Not Started", "$50K", "Feed Nov 12 reveal"),
        ("2026-10-27", "Retention", "Customer Proof", "Post-panel nurture + case study draft", "Christy", "Not Started", "$30K", ""),
    ]
    build_weekly_calendar(wb, "October 2026", oct_weeks)

    build_social(wb)
    build_webinars(wb)
    build_field_events(wb)
    build_pipeline(wb)
    build_decisions(wb)
    build_measurement(wb)
    build_q4_outline(wb)

    out = "/workspace/docs/marketing/Q3-Q4-2026-Marketing-Plan-Tracker.xlsx"
    wb.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
