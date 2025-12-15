import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="LQR Road Map to SUCCESS",
    page_icon="🏠",
    layout="centered",
)

# ----- LQR Brand Palette (derived from your provided logo) -----
ACCENT = "#036BDA"
ACCENT_STRONG = "#125DAD"
TEXT_MAIN = "#F9FAFB"
TEXT_MUTED = "#9CA3AF"
BG_1 = "#050814"
BG_2 = "#0B1226"
BORDER = "rgba(31,41,55,.95)"

LOGO_DATA_URI = "data:image/png;base64,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JtP+9Ysuuoh4PM59991HOBzusG0sFuPiiy9m/mfzOO2007jp5j/u0LX34K3qmZxzbrcW1/4icr63nalTt3+6Aufo7N7ab7ujg5LFf52WGtLXXGlpKQBDhgzZ7h+gbdu88847zJ8/HwCv18u3vvUtqqqqstssXLiQmTNnYqXSBUf6V1dXc8YZZwCwePFiPvjgAyItrR22tW2byZMns+uuuwJw7733EosVWPqhQOFaX1/Pr371K3w+H+vXr2f69OmkEkm0gj322IMTTjihw2HWr19PLBZjt91Hdmt6oeenTeOQQ8fTt2/fvOfj8TgzZsxgzZo1YHec7cDr9XLFFVds973OvJ5Op/n+RReTTKe45557OgSjzLahUIgpU6Zw/S9+yXPPPUckGuW222/DNJ3ZM5qamnj++eepr69HaSgtL+PCCy/MHiNTKG/ZvJnpL04n2hLB9HoYN24chx9+eIdz1tfXU1NTw5gxYzoNMHV1dUyfPp2mpiaUhnBpCZMmTWLQoEF558x49913ndq6Bp/fx8RJkxg+fDgAd/z978STCbxeb8F92/vhD3/IggULePvtt7FtZz69M888kyHVQ7I/30zgWblyJS9OfxEUjBgxglNOOaXT44riJkkN/yO600luGAZHHXUUq1at4u677+bwww/PBqPM/mPGjOGcc87h4YcfZt26dYwaNYrq6mqqq6upra1l9erV2e332GMPJk2axD333MMzzzzDIYccwiGHHEJ1dTXLly/PBiOAWbNmUVZWlj1WdXU1zz37LE88/jgDBw6kurqa/v37k0qlmDZtGobh/GoOGTKEY489lvvuu4/169cXDEYADQ0NXHbZZaSSyYKv575PWmseeeQRJ+i0e+/8fj+TJ09m3bp13H333VRUVHDIIYcwZswYKisr2bBhw3bfZ2ibxvWBBx5g9uzZ/O53v6O0tLTLn1MoFOKG39zAkCFDeG3GDD788MPsa+Xl5Zx//vm8+OKLTJ06lfPOOy9v30zh3r9/f84/73ymTZuGbdsFgxHADTfcwJT778/bt73evXtzwQUXMHPmTP71r39x3nnnMXDgwOx7mFtbBDjiiCNIJBLcc889HHDggdlglEqnePOttygtLc3+7IcOHcrz06bxzDPP5P1OpFKp7H2PHTuWY489lqeeeornnnuOIUOG5K3Iody1n3bZdVcef+wxSktK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"

# Make Streamlit chrome blend with the app
st.markdown(f"""<style>
    .stApp {{
        background: radial-gradient(circle at top, {BG_2} 0%, {BG_1} 65%);
        color: {TEXT_MAIN};
    }}
    header[data-testid="stHeader"] {{ background: rgba(0,0,0,0); }}
</style>""", unsafe_allow_html=True)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>LQR Road Map to SUCCESS</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="theme-color" content="{BG_1}" />
  <style>
    :root{{
      --text:{TEXT_MAIN};
      --muted:{TEXT_MUTED};
      --accent:{ACCENT};
      --accent-strong:{ACCENT_STRONG};
      --danger:#f97373;
      --warning:#f59e0b;
      --success:#4ade80;
      --radius:18px;
      --border:{BORDER};
    }}
    *{{box-sizing:border-box}}
    body{{
      margin:0;
      font-family:system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif;
      background:radial-gradient(circle at top,{BG_2} 0,{BG_1} 55%);
      color:var(--text);
      min-height:100vh;
      display:flex;
      flex-direction:column;
    }}
    header{{
      padding:1rem 1.25rem .75rem;
      border-bottom:1px solid rgba(15,23,42,.75);
      background:linear-gradient(135deg,rgba(15,23,42,.96),rgba(15,23,42,.85));
      backdrop-filter:blur(18px);
      position:sticky;top:0;z-index:10;
    }}
    .title-row{{display:flex;align-items:center;justify-content:space-between;gap:.75rem}}
    .brand{{display:flex;align-items:center;gap:.75rem}}
    .brand img{{height:42px;width:auto;display:block}}
    h1{{margin:0;font-size:1.12rem;letter-spacing:.03em;text-transform:uppercase}}
    h1 span{{font-weight:700;color:var(--accent)}}
    .subtitle{{margin:.3rem 0 0;font-size:.82rem;color:var(--muted)}}
    .pill{{
      border-radius:999px;
      padding:.32rem .8rem;
      border:1px solid rgba(3,107,218,.35);
      background:radial-gradient(circle at top left,rgba(3,107,218,.22),rgba(15,23,42,.95));
      font-size:.7rem;text-transform:uppercase;letter-spacing:.09em;
      display:inline-flex;align-items:center;gap:.35rem;white-space:nowrap;
    }}
    .dot{{width:6px;height:6px;border-radius:999px;background:var(--success);box-shadow:0 0 0 6px rgba(34,197,94,.28)}}
    main{{flex:1;padding:.75rem 1rem 4.7rem;max-width:860px;width:100%;margin:0 auto}}
    .view{{display:none}}
    .view.active{{display:block;animation:fadeIn .2s ease-out}}
    @keyframes fadeIn{{from{{opacity:0;transform:translateY(4px)}}to{{opacity:1;transform:translateY(0)}}}}
    .section-heading{{display:flex;align-items:baseline;justify-content:space-between;gap:1rem;margin:.25rem 0 .65rem}}
    .section-heading h2{{font-size:1.12rem;margin:0}}
    .desc{{font-size:.86rem;color:var(--muted);margin:.15rem 0 .85rem}}
    .grid{{display:grid;gap:.75rem}}
    .card{{
      background:radial-gradient(circle at top left,rgba(15,23,42,.35),rgba(2,6,23,.96));
      border-radius:var(--radius);
      border:1px solid rgba(15,23,42,.95);
      box-shadow:0 12px 30px rgba(15,23,42,.85);
      padding:.9rem .9rem .75rem;
      cursor:pointer;
      transition:transform .12s ease-out,border-color .12s ease-out;
    }}
    .card:hover{{transform:translateY(-2px);border-color:rgba(3,107,218,.45)}}
    .card-header{{display:flex;align-items:center;justify-content:space-between;gap:.5rem;margin-bottom:.35rem}}
    .card-title{{font-size:.93rem;font-weight:750}}
    .icon{{
      width:28px;height:28px;border-radius:999px;
      display:inline-flex;align-items:center;justify-content:center;
      font-size:1rem;
      background:radial-gradient(circle at top,rgba(3,107,218,.18),rgba(15,23,42,.92));
      border:1px solid rgba(3,107,218,.45);
      flex-shrink:0;
    }}
    .card-body{{font-size:.8rem;color:var(--muted)}}
    .card-footer{{display:flex;align-items:center;justify-content:space-between;margin-top:.55rem;font-size:.75rem;color:var(--muted)}}
    .badge{{
      border-radius:999px;
      padding:.15rem .5rem;
      font-size:.66rem;
      text-transform:uppercase;
      letter-spacing:.08em;
      border:1px solid rgba(75,85,99,.9);
      color:var(--muted);
      white-space:nowrap;
    }}
    .badge.danger{{border-color:rgba(249,115,115,.9);color:#fca5a5}}
    .badge.warning{{border-color:rgba(245,158,11,.9);color:#fbbf24}}
    .badge.accent{{border-color:rgba(3,107,218,.9);color:var(--accent)}}
    .badge.success{{border-color:rgba(74,222,128,.9);color:#86efac}}
    .block{{
      background:linear-gradient(145deg,rgba(15,23,42,.92),rgba(15,23,42,.8));
      border-radius:var(--radius);
      padding:.85rem .9rem;
      border:1px solid rgba(15,23,42,.95);
      box-shadow:0 12px 26px rgba(15,23,42,.9);
      margin-bottom:.8rem;
    }}
    .block h3{{margin:0 0 .35rem;font-size:.95rem}}
    .block h4{{margin:.35rem 0 .25rem;font-size:.88rem}}
    ul.compact{{margin:.25rem 0 .3rem 1.1rem;padding:0;font-size:.82rem;color:var(--muted)}}
    ul.compact li{{margin-bottom:.15rem}}
    .back-row{{display:flex;align-items:center;justify-content:space-between;margin-bottom:.4rem;gap:.75rem}}
    .back{{display:inline-flex;align-items:center;gap:.25rem;font-size:.78rem;color:var(--muted);cursor:pointer}}
    .back:hover{{color:var(--accent)}}
    .callout{{
      border-radius:12px;
      border:1px dashed rgba(3,107,218,.65);
      background:rgba(3,107,218,.10);
      padding:.55rem .65rem;
      margin-top:.45rem;
      color:#dbeafe;
      font-size:.8rem;
    }}
    footer.nav{{
      position:fixed;bottom:0;left:0;right:0;
      background:linear-gradient(180deg,rgba(15,23,42,.94),rgba(2,6,23,.98));
      border-top:1px solid var(--border);
      padding:.3rem .75rem .55rem;
      z-index:15;
      backdrop-filter:blur(18px);
    }}
    .nav-row{{
      max-width:720px;margin:0 auto;
      display:flex;justify-content:space-between;align-items:center;gap:.5rem;
    }}
    .nav-btn{{
      flex:1;
      border-radius:999px;
      padding:.35rem .5rem;
      font-size:.75rem;
      border:1px solid rgba(51,65,85,.9);
      cursor:pointer;
      background:rgba(15,23,42,.98);
      color:var(--muted);
      display:inline-flex;align-items:center;justify-content:center;gap:.35rem;
    }}
    .nav-btn .ico{{font-size:1rem}}
    .nav-btn.active{{
      background:radial-gradient(circle at top,rgba(3,107,218,.32),rgba(15,23,42,.98));
      color:#e0f2fe;
      border-color:rgba(3,107,218,.95);
    }}
    .doclink{{
      display:inline-block;
      width:100%;
      padding:.55rem .7rem;
      border-radius:12px;
      border:1px solid rgba(3,107,218,.35);
      background:rgba(3,107,218,.08);
      color:#e0f2fe;
      text-decoration:none;
      margin:.2rem 0;
      font-size:.82rem;
    }}
    .doclink:hover{{border-color:rgba(3,107,218,.75);background:rgba(3,107,218,.12)}}
  </style>
</head>
<body>
<header>
  <div class="title-row">
    <div class="brand">
      <img src="{LOGO_DATA_URI}" alt="Lifetime Quality Roofing logo" />
      <div>
        <h1>LQR <span>Road Map to SUCCESS</span></h1>
        <p class="subtitle">Pick the bucket. Follow the steps. Win the claim.</p>
      </div>
    </div>
    <div class="pill"><span class="dot"></span><span>Bucket Picker</span></div>
  </div>
</header>

<main>

  <!-- HOME (Buckets only) -->
  <section id="view-home" class="view active">
    <div class="section-heading">
      <h2>Choose the claim bucket</h2>
      <span class="badge accent">5 Buckets</span>
    </div>

    <p class="desc">Start here. If you need docs or visuals, use the bottom navigation (Vault / Training).</p>

    <div class="grid">
      <article class="card" data-view-target="view-bucket-denied">
        <div class="card-header"><div class="icon">🟥</div><div class="card-title">Denied</div></div>
        <div class="card-body">Carrier said no. Force a second look (or end it fast).</div>
        <div class="card-footer"><span><small>Bucket 1</small></span><span>Open ➜</span></div>
      </article>

      <article class="card" data-view-target="view-bucket-components">
        <div class="card-header"><div class="icon">🟧</div><div class="card-title">Components Only</div></div>
        <div class="card-body">They paid parts (vents/flashings/valley) but not shingles.</div>
        <div class="card-footer"><span><small>Bucket 2</small></span><span>Open ➜</span></div>
      </article>

      <article class="card" data-view-target="view-bucket-shingles">
        <div class="card-header"><div class="icon">🟨</div><div class="card-title">Shingle Repairs</div></div>
        <div class="card-body">Spot repairs approved. Prove repairability & CAR, then expand.</div>
        <div class="card-footer"><span><small>Bucket 3</small></span><span>Open ➜</span></div>
      </article>

      <article class="card" data-view-target="view-bucket-slopes">
        <div class="card-header"><div class="icon">🟦</div><div class="card-title">Slope Approval</div></div>
        <div class="card-body">Some slopes paid, others denied. Win with connections & continuity.</div>
        <div class="card-footer"><span><small>Bucket 4</small></span><span>Open ➜</span></div>
      </article>

      <article class="card" data-view-target="view-bucket-full">
        <div class="card-header"><div class="icon">🟩</div><div class="card-title">Full Roof Approval</div></div>
        <div class="card-body">Claim won. Validate scope, prevent surprises, set expectations.</div>
        <div class="card-footer"><span><small>Bucket 5</small></span><span>Open ➜</span></div>
      </article>
    </div>

    <div class="callout"><strong>Rule:</strong> Identify the bucket first. Then follow the steps in order. No free-styling.</div>
  </section>

  <!-- BUCKET SCREENS -->
  <section id="view-bucket-denied" class="view">
    <div class="back-row"><div class="back" data-view-target="view-home">← Back to Buckets</div><span class="badge danger">Denied</span></div>
    <div class="section-heading"><h2>Denied Claim</h2></div>
    <p class="desc">The carrier said no. Don’t guess. Don’t spiral. Follow the steps.</p>

    <div class="block">
      <h3>You’re in this bucket if…</h3>
      <ul class="compact"><li>The carrier denied the roof.</li><li>No roof scope was approved.</li><li>Collateral may or may not have been paid.</li></ul>
      <div class="callout"><strong>Mindset:</strong> Denial ≠ dead claim. This is evidence + homeowner-driven.</div>
    </div>

    <div class="block">
      <h3>Your goal</h3>
      <p class="desc"><strong>Get the carrier to take a second look</strong> — or determine early the claim is not viable.</p>
      <h4>Success exit</h4>
      <p class="desc">✔ Reinspection scheduled or desk/supervisor review confirmed → move to the new bucket the carrier creates.</p>
    </div>

    <div class="block">
      <h3>Step-by-step road map</h3>
      <h4>Step 1: Identify why it was denied</h4>
      <ul class="compact"><li>Cause denial</li><li>Date of loss denial</li><li>Mixed denial</li></ul>

      <h4>Step 2: Pick the correct leverage</h4>
      <ul class="compact">
        <li><strong>Cause</strong> → Damage ID + strong photo reports.</li>
        <li><strong>Date</strong> → weather history + clean homeowner timeline.</li>
        <li><strong>Mixed</strong> → simplify the story and remove noise.</li>
      </ul>

      <h4>Step 3: Align the homeowner</h4>
      <ul class="compact"><li>Explain denial in plain language.</li><li>Set expectations (not guaranteed).</li><li>Give the homeowner the words + attachments.</li></ul>

      <h4>Step 4: Ask for the right next step</h4>
      <ul class="compact"><li>Reinspection</li><li>Supervisor review</li><li>Desk review with new evidence</li></ul>

      <div class="callout"><strong>Common mistakes:</strong> Don’t argue matching. Don’t ask full roof first. Don’t fight the carrier for the homeowner.</div>
    </div>

    <div class="block">
      <h3>Recommended Docs (Tap to Open)</h3>
      <ul class="compact">
        <li><a class="doclink" href="./vault/Claim%20Success/Direct%20Physical%20Damage%20Argument.docx" target="_blank" download>Direct Physical Damage Argument (DOCX)</a></li>
        <li><a class="doclink" href="./vault/Claim%20Success/Engineer%20Testing%20Repairability.pdf" target="_blank" download>Engineer Testing Repairability (PDF)</a></li>
        <li><a class="doclink" href="./vault/Claim%20Success/DMI%20Initial%20Response.docx" target="_blank" download>DMI Initial Response (DOCX)</a></li>
        <li><a class="doclink" href="./vault/Claim%20Success/DMI%20Follow%20UP%20Response.docx" target="_blank" download>DMI Follow-Up Response (DOCX)</a></li>
        <li><a class="doclink" href="./vault/Claim%20Success/IRC%20Outline.pdf" target="_blank" download>IRC Outline (Reference) (PDF)</a></li>
      </ul>
      <div class="callout"><strong>Tip:</strong> If a link doesn’t open, use the Vault tab and search for the same title.</div>
    </div>
  </section>

  <section id="view-bucket-components" class="view">
    <div class="back-row">
      <div class="back" data-view-target="view-home">← Back to Buckets</div>
      <span class="badge warning">Components Only</span>
    </div>

    <div class="section-heading">
      <h2>Bucket 2 — Components Only</h2>
    </div>

    <div class="callout">
      <strong>Core Rule:</strong> If a component is approved, shingles are always impacted.
    </div>

    <div class="block">
      <h3>You’re in this bucket if…</h3>
      <ul class="compact">
        <li>The carrier approved one or more roof components</li>
        <li>No roofing material is included in the scope</li>
        <li>The approved work cannot be completed without disturbing shingles</li>
      </ul>
    </div>

    <div class="block">
      <h3>Component Groups (Foundational Concept)</h3>
      <p class="desc">Tap a group to open the playbook.</p>

      <div class="grid">
        <article class="card" data-view-target="view-components-vents">
          <div class="card-header"><div class="icon">🌀</div><div class="card-title">Vents</div></div>
          <div class="card-body">Pipe jacks, turtle/box vents, bath fan vents, ridge vent sections.</div>
          <div class="card-footer"><span><small>Playbook</small></span><span>Open ➜</span></div>
        </article>

        <article class="card" data-view-target="view-components-flashings">
          <div class="card-header"><div class="icon">🧱</div><div class="card-title">Flashings</div></div>
          <div class="card-body">Chimney, skylight kits, wall/headwall, dormers.</div>
          <div class="card-footer"><span><small>Playbook</small></span><span>Open ➜</span></div>
        </article>

        <article class="card" data-view-target="view-components-valleys">
          <div class="card-header"><div class="icon">💧</div><div class="card-title">Valleys</div></div>
          <div class="card-body">Open metal, closed-cut, woven valleys; primary water channels.</div>
          <div class="card-footer"><span><small>Playbook</small></span><span>Open ➜</span></div>
        </article>
      </div>
    </div>

    <div class="block">
      <h3>The Question That Drives Every Components Claim</h3>
      <div class="callout">
        “How are we expected to remove and replace this component without affecting the surrounding roofing material?”
      </div>
    </div>

    <div class="block">
      <h3>Next Step Logic</h3>
      <ul class="compact">
        <li>If roofing material is added → Move to <strong>Shingle Repairs</strong></li>
        <li>If repairs are not reasonable → Escalate toward <strong>Slope Approval</strong></li>
        <li>If scope direction is unclear → Request written clarification or reinspection</li>
      </ul>
    </div>
  </section>

  <!-- The rest of your sections remain as-is; trim/add as you like -->

</main>

<footer class="nav">
  <div class="nav-row">
    <button class="nav-btn active" data-view-target="view-home"><span class="ico">🧺</span><span>Buckets</span></button>
    <button class="nav-btn" data-view-target="view-vault"><span class="ico">🔎</span><span>Vault</span></button>
    <button class="nav-btn" data-view-target="view-training"><span class="ico">📚</span><span>Training</span></button>
  </div>
</footer>

<script>
(function(){
  const views = document.querySelectorAll(".view");
  function showView(id){
    views.forEach(v=>v.classList.remove("active"));
    const t = document.getElementById(id);
    if(t) t.classList.add("active");
    document.querySelectorAll(".nav-btn").forEach(btn=>{
      const tgt = btn.getAttribute("data-view-target");
      btn.classList.toggle("active", tgt === id);
    });
    window.scrollTo({top:0,behavior:"instant"});
  }
  document.body.addEventListener("click",(e)=>{
    const el = e.target.closest("[data-view-target]");
    if(!el) return;
    const id = el.getAttribute("data-view-target");
    if(!id) return;
    showView(id);
  });
  window._lqrShowView = showView;
})();
</script>
</body>
</html>"""

components.html(html, height=1400, scrolling=True)
