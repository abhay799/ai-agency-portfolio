import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="AetherFlow AI — Indian B2B & D2C AI Automation Agency")

FOUNDER_NAME = os.getenv("FOUNDER_NAME", "Abhay Kumar")
AGENCY_NAME = os.getenv("AGENCY_NAME", "AetherFlow AI Studio")
WHATSAPP_NUMBER = os.getenv("WHATSAPP_NUMBER", "919876543210")

# Live Render Demo URLs (override via Render Environment Variables anytime)
DEMO_URLS = {
    "support": os.getenv("URL_SUPPORT", "https://ai-customer-support-agent1.onrender.com"),
    "revenue": os.getenv("URL_REVENUE", "https://lead-crm-appointment-ai-2.onrender.com"),
    "invoice": os.getenv("URL_INVOICE", "https://invoice-automation-ai.onrender.com"),
    "recruit": os.getenv("URL_RECRUIT", "https://recruitment-automation-gq47.onrender.com"),
    "email": os.getenv("URL_EMAIL", "https://email-automation-ai.onrender.com"),
    "workflow": os.getenv("URL_WORKFLOW", "https://workflow-automation-ai.onrender.com"),
    "report": os.getenv("URL_REPORT", "https://report-automation-ai.onrender.com"),
}


@app.get("/health")
async def health():
    return {"status": "live", "agency": AGENCY_NAME, "founder": FOUNDER_NAME, "demos": len(DEMO_URLS)}


@app.get("/", response_class=HTMLResponse)
async def agency_hub():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{AGENCY_NAME} — Practical AI Agents for Indian Businesses</title>
  <style>
    :root {{
      --bg: #090d16;
      --surface: #111827;
      --surface-2: #1e293b;
      --border: #1f2937;
      --text: #f8fafc;
      --muted: #94a3b8;
      --accent: #3b82f6;
      --accent-2: #10b981;
      --warn: #f59e0b;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
    body {{ background: var(--bg); color: var(--text); line-height: 1.55; }}
    a {{ color: inherit; text-decoration: none; }}
    .container {{ max-width: 1080px; margin: 0 auto; padding: 0 18px; }}

    /* Top Nav */
    .nav {{ position: sticky; top: 0; z-index: 40; background: rgba(9, 13, 22, 0.92); backdrop-filter: blur(10px); border-bottom: 1px solid var(--border); }}
    .nav-inner {{ display: flex; justify-content: space-between; align-items: center; padding: 14px 18px; max-width: 1080px; margin: 0 auto; }}
    .brand {{ font-weight: 700; font-size: 16px; display: flex; align-items: center; gap: 8px; }}
    .brand-badge {{ background: linear-gradient(135deg, #2563eb, #10b981); color: #fff; padding: 4px 8px; border-radius: 7px; font-size: 12px; font-weight: 800; }}
    .nav-cta {{ background: var(--accent); color: #fff; padding: 8px 14px; border-radius: 8px; font-size: 13px; font-weight: 600; }}

    /* Hero */
    .hero {{ padding: 46px 0 34px; text-align: center; }}
    .pill {{ display: inline-flex; align-items: center; gap: 6px; background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.35); color: #34d399; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 600; margin-bottom: 16px; }}
    .hero h1 {{ font-size: clamp(26px, 5vw, 42px); font-weight: 800; letter-spacing: -0.02em; line-height: 1.18; max-width: 820px; margin: 0 auto 14px; }}
    .hero p {{ color: var(--muted); font-size: 15px; max-width: 650px; margin: 0 auto 24px; }}
    .hero-btns {{ display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; }}
    .btn-primary {{ background: var(--accent); color: #fff; padding: 12px 20px; border-radius: 10px; font-weight: 600; font-size: 14px; border: none; cursor: pointer; }}
    .btn-secondary {{ background: var(--surface-2); color: #fff; padding: 12px 20px; border-radius: 10px; font-weight: 600; font-size: 14px; border: 1px solid #334155; cursor: pointer; }}

    /* Stats Strip */
    .stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px; margin: 28px 0 40px; }}
    .stat-card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 14px; text-align: center; }}
    .stat-num {{ font-size: 20px; font-weight: 800; color: #38bdf8; }}
    .stat-lbl {{ font-size: 12px; color: var(--muted); margin-top: 2px; }}

    /* Section Headers */
    .sec-head {{ margin-bottom: 18px; }}
    .sec-head h2 {{ font-size: 22px; font-weight: 700; }}
    .sec-head p {{ color: var(--muted); font-size: 14px; margin-top: 4px; }}

    /* Filter Tabs */
    .filters {{ display: flex; gap: 8px; overflow-x: auto; padding-bottom: 12px; margin-bottom: 16px; scrollbar-width: none; }}
    .filters::-webkit-scrollbar {{ display: none; }}
    .f-btn {{ flex-shrink: 0; background: var(--surface); color: var(--muted); border: 1px solid var(--border); padding: 7px 13px; border-radius: 999px; font-size: 12px; font-weight: 600; cursor: pointer; }}
    .f-btn.active {{ background: var(--accent); color: #fff; border-color: var(--accent); }}

    /* Demo Grid */
    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 14px; margin-bottom: 44px; }}
    .card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 14px; padding: 18px; display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.15s ease, border-color 0.15s ease; }}
    .card:hover {{ transform: translateY(-2px); border-color: #3b82f6; }}
    .card-top {{ display: flex; justify-content: space-between; align-items: flex-start; gap: 8px; margin-bottom: 10px; }}
    .tag {{ font-size: 11px; font-weight: 700; padding: 3px 8px; border-radius: 6px; background: rgba(59, 130, 246, 0.16); color: #60a5fa; }}
    .price-pill {{ font-size: 11px; font-weight: 700; color: #34d399; background: rgba(16, 185, 129, 0.14); padding: 3px 8px; border-radius: 6px; }}
    .card h3 {{ font-size: 16px; font-weight: 700; margin-bottom: 6px; }}
    .card p {{ font-size: 13px; color: var(--muted); margin-bottom: 12px; }}
    .bullets {{ list-style: none; font-size: 12px; color: #cbd5e1; margin-bottom: 16px; }}
    .bullets li {{ margin-bottom: 5px; padding-left: 14px; position: relative; }}
    .bullets li::before {{ content: "✓"; position: absolute; left: 0; color: var(--accent-2); font-weight: 700; }}
    .card-actions {{ display: flex; gap: 8px; }}
    .btn-live {{ flex: 1; text-align: center; background: var(--accent); color: #fff; padding: 9px 12px; border-radius: 8px; font-size: 13px; font-weight: 600; }}
    .btn-embed {{ background: var(--surface-2); color: #e2e8f0; border: 1px solid #334155; padding: 9px 11px; border-radius: 8px; font-size: 12px; font-weight: 600; cursor: pointer; }}

    /* ROI Calculator */
    .roi-box {{ background: var(--surface); border: 1px solid var(--border); border-radius: 16px; padding: 20px; margin-bottom: 44px; }}
    .roi-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px; margin-top: 14px; align-items: center; }}
    .slider-grp {{ margin-bottom: 12px; }}
    .slider-grp label {{ display: flex; justify-content: space-between; font-size: 13px; font-weight: 600; margin-bottom: 6px; }}
    .slider-grp input {{ width: 100%; accent-color: var(--accent); }}
    .roi-result {{ background: #0b1220; border: 1px solid #1e3a8a; border-radius: 12px; padding: 16px; text-align: center; }}
    .roi-big {{ font-size: 28px; font-weight: 800; color: #34d399; margin: 4px 0; }}

    /* Pricing */
    .pricing {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); gap: 14px; margin-bottom: 44px; }}
    .p-card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 14px; padding: 20px; display: flex; flex-direction: column; justify-content: space-between; }}
    .p-card.featured {{ border: 2px solid var(--accent); position: relative; }}
    .p-title {{ font-size: 14px; font-weight: 700; color: #60a5fa; text-transform: uppercase; }}
    .p-price {{ font-size: 26px; font-weight: 800; margin: 8px 0 4px; }}
    .p-sub {{ font-size: 12px; color: var(--muted); margin-bottom: 14px; }}

    /* Footer */
    .footer {{ border-top: 1px solid var(--border); padding: 24px 0 40px; text-align: center; color: var(--muted); font-size: 13px; }}
  </style>
</head>
<body>
  <nav class="nav">
    <div class="nav-inner">
      <div class="brand"><span class="brand-badge">AI</span> {AGENCY_NAME}</div>
      <a class="nav-cta" href="#pricing">Plans from ₹4,999</a>
    </div>
  </nav>

  <main class="container">
    <section class="hero">
      <div class="pill">● Live Production Demos &bull; Built in Bengaluru for Indian Businesses</div>
      <h1>Automate Repetitive Support, Leads &amp; Daily Ops Starting at ₹4,999</h1>
      <p>Test 10 live AI workflows right in your browser—complete with tool calling, GST validation, CRM sync, and 1-line website embedding. Live for your business in 3–5 days.</p>
      <div class="hero-btns">
        <a href="#demos" class="btn-primary">Test Live AI Demos ↓</a>
        <button class="btn-secondary" onclick="bookAudit('Free 15-Min AI Workflow Audit')">Book Free 15-Min Demo</button>
      </div>

      <div class="stats">
        <div class="stat-card"><div class="stat-num">10 Workflows</div><div class="stat-lbl">Live &amp; Interactive</div></div>
        <div class="stat-card"><div class="stat-num">3–5 Days</div><div class="stat-lbl">Custom Setup</div></div>
        <div class="stat-card"><div class="stat-num">₹4,999</div><div class="stat-lbl">Starter Pilot Setup</div></div>
        <div class="stat-card"><div class="stat-num">99.9% Uptime</div><div class="stat-lbl">Multi-Model Fallback</div></div>
      </div>
    </section>

    <section id="demos">
      <div class="sec-head">
        <h2>Interactive Live Agent Portfolio</h2>
        <p>Tap <b>Launch Live Demo</b> on any card to test real tool execution, or copy the 1-line embed script.</p>
      </div>

      <div class="filters">
        <button class="f-btn active" onclick="filterCards('all', this)">All 10 Workflows</button>
        <button class="f-btn" onclick="filterCards('d2c', this)">D2C &amp; Support (#1–#2)</button>
        <button class="f-btn" onclick="filterCards('growth', this)">Lead, CRM &amp; Appts (#3–#5)</button>
        <button class="f-btn" onclick="filterCards('ops', this)">Email, GST &amp; Ops (#6–#9)</button>
        <button class="f-btn" onclick="filterCards('hr', this)">HR &amp; Hiring (#10)</button>
      </div>

      <div class="grid" id="demoGrid">
        <!-- #1 & #2 -->
        <div class="card" data-cat="d2c">
          <div>
            <div class="card-top"><span class="tag">#1 &amp; #2 &bull; D2C &amp; WhatsApp Support</span><span class="price-pill">₹4,999 Setup</span></div>
            <h3>VastraVibe D2C Support &amp; Returns Agent</h3>
            <p>Resolves WISMO order tracking, 7-day reverse pickups, COD policies, and escalates priority tickets 24/7.</p>
            <ul class="bullets">
              <li>Live Delhivery/Blue Dart AWB lookup + RMA generator</li>
              <li>Human escalation ticket queue with SLA tracking</li>
              <li>1-line floating chat widget for Shopify &amp; WooCommerce</li>
            </ul>
          </div>
          <div class="card-actions">
            <a class="btn-live" href="{DEMO_URLS['support']}" target="_blank">Launch Live Demo ↗</a>
            <button class="btn-embed" onclick="copyWidget('{DEMO_URLS['support']}')">&lt;/&gt; Embed</button>
          </div>
        </div>

        <!-- #3, #4, #5 -->
        <div class="card" data-cat="growth">
          <div>
            <div class="card-top"><span class="tag">#3 + #4 + #5 &bull; Revenue Engine</span><span class="price-pill">₹11,999 Setup</span></div>
            <h3>Lead-to-CRM-to-Appointment AI Agent</h3>
            <p>Captures inbound inquiries, scores buyer intent (0–100), updates CRM stages, and books calendar slots.</p>
            <ul class="bullets">
              <li>Instant HOT/WARM lead scoring in INR budgets</li>
              <li>Auto-syncs CRM stage to "Appointment Booked"</li>
              <li>Built for Clinics, Real Estate, Interiors &amp; Coaching</li>
            </ul>
          </div>
          <div class="card-actions">
            <a class="btn-live" href="{DEMO_URLS['revenue']}" target="_blank">Launch Live Demo ↗</a>
            <button class="btn-embed" onclick="copyWidget('{DEMO_URLS['revenue']}')">&lt;/&gt; Embed</button>
          </div>
        </div>

        <!-- #7 -->
        <div class="card" data-cat="ops">
          <div>
            <div class="card-top"><span class="tag">#7 &bull; Finance &amp; GST Audit</span><span class="price-pill">₹7,999 Setup</span></div>
            <h3>BillGuard GST Invoice &amp; 3-Way PO Auditor</h3>
            <p>Extracts vendor GSTIN, taxable base, CGST/SGST/IGST, and catches PO overcharges before payout.</p>
            <ul class="bullets">
              <li>15-digit Indian GSTIN regex &amp; duplicate bill check</li>
              <li>Flags hidden tax/PO variances automatically</li>
              <li>Live Input Tax Credit (ITC) &amp; payout ledger</li>
            </ul>
          </div>
          <div class="card-actions">
            <a class="btn-live" href="{DEMO_URLS['invoice']}" target="_blank">Launch Live Demo ↗</a>
            <button class="btn-embed" onclick="bookAudit('BillGuard GST Invoice AI (₹7,999)')">Request Custom</button>
          </div>
        </div>

        <!-- #10 -->
        <div class="card" data-cat="hr">
          <div>
            <div class="card-top"><span class="tag">#10 &bull; Recruitment &amp; ATS</span><span class="price-pill">₹5,999 Setup</span></div>
            <h3>HirePulse AI Resume Screener &amp; L1 Scheduler</h3>
            <p>Scores candidate resumes (0–100) against job roles, checks LPA/notice fit, and books Google Meet L1s.</p>
            <ul class="bullets">
              <li>Instant skill-gap &amp; CTC budget fit detection</li>
              <li>Generates 3 tailored technical screening questions</li>
              <li>Live ATS candidate leaderboard &amp; interview tracker</li>
            </ul>
          </div>
          <div class="card-actions">
            <a class="btn-live" href="{DEMO_URLS['recruit']}" target="_blank">Launch Live Demo ↗</a>
            <button class="btn-embed" onclick="bookAudit('HirePulse Recruitment AI (₹5,999)')">Request Custom</button>
          </div>
        </div>

        <!-- #6 -->
        <div class="card" data-cat="ops">
          <div>
            <div class="card-top"><span class="tag">#6 &bull; Inbox &amp; Sales Ops</span><span class="price-pill">₹4,999 Setup</span></div>
            <h3>ApexMail B2B Email Triage &amp; Auto-Reply</h3>
            <p>Classifies incoming B2B quotes, logistics escalations, and vendor bills, routing tasks and drafting replies.</p>
            <ul class="bullets">
              <li>Auto-routes tasks to Sales, Ops, or Accounts teams</li>
              <li>Drafts GST-ready wholesale quotes in seconds</li>
              <li>One-click executive reply clipboard &amp; task board</li>
            </ul>
          </div>
          <div class="card-actions">
            <a class="btn-live" href="{DEMO_URLS['email']}" target="_blank">Launch Live Demo ↗</a>
            <button class="btn-embed" onclick="bookAudit('ApexMail Email AI (₹4,999)')">Request Custom</button>
          </div>
        </div>

        <!-- #8 & #9 -->
        <div class="card" data-cat="ops">
          <div>
            <div class="card-top"><span class="tag">#8 &amp; #9 &bull; ERP Workflows &amp; MIS</span><span class="price-pill">₹9,999 Setup</span></div>
            <h3>FlowOps Orchestrator &amp; PulseBoard MIS AI</h3>
            <p>Automates COD RTO checks, dark-store stock transfers, and daily P&amp;L / ROAS anomaly reports.</p>
            <ul class="bullets">
              <li>Multi-step SOP execution with timestamped audit trail</li>
              <li>Detects COD RTO spikes &amp; bleeding ad campaigns</li>
              <li>WhatsApp/Slack-ready daily founder MIS digests</li>
            </ul>
          </div>
          <div class="card-actions">
            <a class="btn-live" href="{DEMO_URLS['report']}" target="_blank">Launch MIS Demo ↗</a>
            <a class="btn-embed" href="{DEMO_URLS['workflow']}" target="_blank">Workflows ↗</a>
          </div>
        </div>
      </div>
    </section>

    <!-- ROI Calculator -->
    <section class="roi-box">
      <div class="sec-head">
        <h2>Client ROI &amp; Team Hours Saved Calculator</h2>
        <p>Estimate monthly operational savings before starting a ₹4,999 pilot.</p>
      </div>
      <div class="roi-grid">
        <div>
          <div class="slider-grp">
            <label><span>Daily Inquiries / Invoices / Resumes</span><span id="volVal">120 / day</span></label>
            <input type="range" id="volRange" min="20" max="500" step="10" value="120" oninput="calcRoi()" />
          </div>
          <div class="slider-grp">
            <label><span>Avg Manual Handling Time</span><span id="minVal">6 mins</span></label>
            <input type="range" id="minRange" min="2" max="20" step="1" value="6" oninput="calcRoi()" />
          </div>
          <div class="slider-grp">
            <label><span>Ops / Support Team Hourly Cost (INR)</span><span id="costVal">₹250 / hr</span></label>
            <input type="range" id="costRange" min="150" max="800" step="25" value="250" oninput="calcRoi()" />
          </div>
        </div>
        <div class="roi-result">
          <div style="font-size:12px;color:#94a3b8;text-transform:uppercase;font-weight:700;">Estimated Monthly Savings (80% Automated)</div>
          <div class="roi-big" id="saveMoney">₹72,000 / mo</div>
          <div style="font-size:13px;color:#cbd5e1;" id="saveHours">288 manual hours reclaimed every month</div>
          <button class="btn-primary" style="margin-top:12px;width:100%;" onclick="bookAudit('Starter Pilot (₹4,999)')">Start ₹4,999 Pilot Today</button>
        </div>
      </div>
    </section>

    <!-- Pricing -->
    <section id="pricing">
      <div class="sec-head">
        <h2>Practical Indian Business Packages (INR)</h2>
        <p>Low upfront setup with optional monthly hosting &amp; API care—built for fast ROI.</p>
      </div>
      <div class="pricing">
        <div class="p-card">
          <div>
            <div class="p-title">Starter Pilot</div>
            <div class="p-price">₹4,999</div>
            <div class="p-sub">One-time setup &bull; Optional ₹1,499/mo care &amp; hosting</div>
            <ul class="bullets">
              <li>1 Custom AI Agent (Support, Lead Bot, Email, or ATS)</li>
              <li>Trained on your exact catalog, FAQ &amp; INR pricing</li>
              <li>1-line website chat widget + WhatsApp webhook ready</li>
              <li>Delivered in 3 days with 14 days support included</li>
            </ul>
          </div>
          <button class="btn-secondary" style="width:100%;" onclick="bookAudit('Starter Pilot (₹4,999)')">Start Starter Pilot</button>
        </div>

        <div class="p-card featured">
          <div>
            <div class="p-title">Growth Revenue Suite (Most Popular)</div>
            <div class="p-price">₹11,999</div>
            <div class="p-sub">One-time setup &bull; Optional ₹2,499/mo care &amp; hosting</div>
            <ul class="bullets">
              <li>Unified Lead Gen + CRM Sync + Appointment Booking Agent</li>
              <li>Google Sheets / Zoho / HubSpot / WhatsApp integration</li>
              <li>Multi-model failover engine for 99.9% uptime</li>
              <li>Delivered in 5 days with 30 days priority tuning</li>
            </ul>
          </div>
          <button class="btn-primary" style="width:100%;" onclick="bookAudit('Growth Revenue Suite (₹11,999)')">Book Growth Suite</button>
        </div>

        <div class="p-card">
          <div>
            <div class="p-title">Custom Operations Stack</div>
            <div class="p-price">₹24,999</div>
            <div class="p-sub">Multi-agent workflow setup &bull; Optional ₹3,999/mo SLA</div>
            <ul class="bullets">
              <li>3+ Integrated Agents (GST Audit + MIS Reports + Support)</li>
              <li>Custom database, ERP &amp; internal dashboard views</li>
              <li>Dedicated cloud deployment &amp; role-based access</li>
              <li>Delivered in 7–10 days with full handover</li>
            </ul>
          </div>
          <button class="btn-secondary" style="width:100%;" onclick="bookAudit('Custom Operations Stack (₹24,999)')">Scope Custom Stack</button>
        </div>
      </div>
    </section>

    <footer class="footer">
      Built by <b>{FOUNDER_NAME}</b> &bull; {AGENCY_NAME} (Bengaluru, India)<br />
      All live demos run on FastAPI + Gemini 3.8 Flash with automatic multi-model failover.
    </footer>
  </main>

  <script>
    function filterCards(cat, btn) {{
      document.querySelectorAll('.f-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      document.querySelectorAll('#demoGrid .card').forEach(card => {{
        card.style.display = (cat === 'all' || card.dataset.cat === cat) ? 'flex' : 'none';
      }});
    }}

    function copyWidget(url) {{
      const tag = `<script src="${{url}}/widget.js"><\\/script>`;
      navigator.clipboard.writeText(tag);
      alert('Copied 1-line website embed script:\\n' + tag);
    }}

    function calcRoi() {{
      const vol = parseInt(document.getElementById('volRange').value, 10);
      const mins = parseInt(document.getElementById('minRange').value, 10);
      const rate = parseInt(document.getElementById('costRange').value, 10);
      document.getElementById('volVal').textContent = vol + ' / day';
      document.getElementById('minVal').textContent = mins + ' mins';
      document.getElementById('costVal').textContent = '₹' + rate + ' / hr';

      const monthlyHoursSaved = Math.round(((vol * mins) / 60) * 30 * 0.8);
      const monthlySavings = monthlyHoursSaved * rate;
      document.getElementById('saveHours').textContent = monthlyHoursSaved.toLocaleString('en-IN') + ' manual hours reclaimed every month';
      document.getElementById('saveMoney').textContent = '₹' + monthlySavings.toLocaleString('en-IN') + ' / mo';
    }}

    function bookAudit(pkg) {{
      const msg = encodeURIComponent(`Hi {FOUNDER_NAME}, I tested your AI demos and want to get started with: ${{pkg}}.`);
      window.open(`https://wa.me/{WHATSAPP_NUMBER}?text=${{msg}}`, '_blank');
    }}

    calcRoi();
  </script>
</body>
</html>"""
