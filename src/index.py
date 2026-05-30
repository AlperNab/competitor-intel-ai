#!/usr/bin/env python3
"""
competitor-intel-ai — competitor URL → positioning analysis, messaging gaps,
pricing strategy, ICP, feature comparison, GTM approach, weaknesses
"""
import anthropic, json, re, sys, urllib.request

SYSTEM = """You are a competitive intelligence analyst and GTM strategist.
Analyze this competitor's positioning, messaging, and strategy.

Return ONLY valid JSON — no markdown, no explanation.

{
  "company_name": "string",
  "url": "string",
  "tagline": "their current tagline",
  "one_liner": "what they actually do in plain English",
  "category": "market category they compete in",
  "positioning": {
    "primary_value_prop": "their #1 claimed benefit",
    "positioning_strategy": "performance|price|trust|innovation|simplicity|customization",
    "tone": "professional|friendly|technical|enterprise|startup",
    "messaging_themes": ["list of recurring themes in their copy"]
  },
  "icp": {
    "company_size": "SMB|mid-market|enterprise|all",
    "industries": ["target industries"],
    "buyer_persona": "who makes the buying decision",
    "pain_points_addressed": ["customer problems they claim to solve"]
  },
  "pricing": {
    "model": "subscription|usage|freemium|one-time|custom|unknown",
    "tiers": ["free|starter|pro|enterprise"],
    "price_signals": "any pricing clues from the page",
    "free_trial": true_or_false
  },
  "features": {
    "core": ["main features prominently featured"],
    "differentiators": ["features they emphasize as unique"],
    "missing_obvious": ["obvious features not mentioned — possible gaps"]
  },
  "social_proof": {
    "customer_logos": ["notable company names if visible"],
    "review_sites_mentioned": ["G2|Capterra|Trustpilot|..."],
    "testimonial_themes": ["what customers praise them for"],
    "case_study_metrics": ["specific numbers from case studies"]
  },
  "gtm": {
    "primary_channel": "SEO|paid|PLG|sales-led|community|partnerships",
    "content_strategy": "description of their content approach",
    "integrations_featured": ["top integrations mentioned"],
    "cta_primary": "main call to action on homepage"
  },
  "weaknesses": [
    {
      "weakness": "observable gap or vulnerability",
      "evidence": "what on the page suggests this",
      "opportunity": "how you could exploit this"
    }
  ],
  "strengths": ["observable competitive advantages"],
  "messaging_gaps": ["topics/pain points they DON'T address that you could own"],
  "keyword_themes": ["main SEO themes from their copy"],
  "battle_card": {
    "headline": "one-liner for your sales team",
    "when_you_see_them": "how they usually come up in deals",
    "your_key_differentiators": ["3 things you do better or differently"],
    "their_objections_to_you": ["what they might say against you"],
    "counter_objections": ["your responses"],
    "trap_questions": ["questions to ask that reveal their weaknesses"]
  },
  "confidence": 0.0
}"""

def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0 competitive-intel/1.0"})
    html = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", errors="replace")
    text = re.sub(r'<script[^>]*>[\s\S]*?</script>','',html,flags=re.I)
    text = re.sub(r'<style[^>]*>[\s\S]*?</style>','',text,flags=re.I)
    text = re.sub(r'<[^>]+>',' ',text)
    text = re.sub(r'\s+',' ',text).strip()
    return text[:35000]

def analyze(url: str, your_product: str = "", your_icp: str = "") -> dict:
    client = anthropic.Anthropic()
    content = fetch(url)
    context = [f"Competitor URL: {url}", f"Content:\n{content}"]
    if your_product: context.append(f"\nOur product: {your_product}")
    if your_icp: context.append(f"Our ICP: {your_icp}")
    context.append("\nAnalyze this competitor completely.")
    resp = client.messages.create(
        model="claude-sonnet-4-20250514", max_tokens=4096, system=SYSTEM,
        messages=[{"role":"user","content":"\n".join(context)}]
    )
    raw = re.sub(r'^```(?:json)?\s*','',resp.content[0].text.strip(),flags=re.MULTILINE)
    raw = re.sub(r'\s*```$','',raw,flags=re.MULTILINE)
    result = json.loads(raw)
    result["url"] = url
    return result

def print_intel(r: dict):
    pos = r.get("positioning",{})
    icp = r.get("icp",{})
    bc = r.get("battle_card",{})
    pricing = r.get("pricing",{})
    print(f"\n{'═'*60}")
    print(f"  COMPETITOR INTEL — {r.get('company_name','?')}")
    print(f"  {r.get('url','')}")
    print(f"{'═'*60}")
    print(f"\n  \"{r.get('tagline','')}\"")
    print(f"  What they do: {r.get('one_liner','')}")
    print(f"  Category: {r.get('category','?')}")
    print(f"\n  Positioning: {pos.get('primary_value_prop','')}")
    print(f"  Strategy: {pos.get('positioning_strategy','?')} | Tone: {pos.get('tone','?')}")
    print(f"\n  ICP: {icp.get('buyer_persona','?')} @ {icp.get('company_size','?')} companies")
    if icp.get("industries"): print(f"  Industries: {', '.join(icp['industries'][:4])}")
    print(f"\n  Pricing: {pricing.get('model','?')}", end="")
    if pricing.get("free_trial"): print(" | Free trial: Yes", end="")
    if pricing.get("price_signals"): print(f" | {pricing['price_signals']}", end="")
    print()

    weaknesses = r.get("weaknesses",[])
    if weaknesses:
        print(f"\n{'─'*60}\n  WEAKNESSES TO EXPLOIT")
        for w in weaknesses:
            print(f"\n  ⚡ {w.get('weakness','')}")
            print(f"     Evidence: {w.get('evidence','')}")
            print(f"     Opportunity: {w.get('opportunity','')}")

    gaps = r.get("messaging_gaps",[])
    if gaps:
        print(f"\n{'─'*60}\n  MESSAGING GAPS (topics they ignore)")
        for g in gaps: print(f"  ○ {g}")

    if bc:
        print(f"\n{'─'*60}\n  BATTLE CARD")
        print(f"  {bc.get('headline','')}")
        if bc.get("your_key_differentiators"):
            print(f"\n  Your advantages:")
            for d in bc["your_key_differentiators"]: print(f"  ✓ {d}")
        if bc.get("trap_questions"):
            print(f"\n  Trap questions to ask:")
            for q in bc["trap_questions"][:3]: print(f"  ? {q}")

    print(f"\n  Confidence: {int(r.get('confidence',0)*100)}%")
    print(f"{'═'*60}\n")

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Competitive intelligence from any URL")
    p.add_argument("url", help="Competitor homepage or product URL")
    p.add_argument("--product","-p",default="",help="Your product description")
    p.add_argument("--icp","-i",default="",help="Your ICP")
    p.add_argument("--json",action="store_true")
    a = p.parse_args()
    r = analyze(a.url, a.product, a.icp)
    if a.json: print(json.dumps(r,indent=2,ensure_ascii=False))
    else: print_intel(r)
