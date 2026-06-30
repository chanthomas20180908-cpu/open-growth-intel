from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml
from jinja2 import Environment, FileSystemLoader


ROOT_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = ROOT_DIR / "templates"

LANDING_TEMPLATE_MAP = {
    "a": "landing/type-a/base.html",
    "b": "landing/type-b/base.html",
    "c": "landing/type-c/base.html",
    "article": "landing/article/base.html",
}


@dataclass(frozen=True)
class LandingBuildRequest:
    page_type: str
    brand_name: str
    output_path: Path
    primary_keyword: Optional[str] = None
    title: Optional[str] = None
    value_prop: Optional[str] = None
    faq_items: Optional[List[Dict[str, str]]] = None


def build_landing_page(request: LandingBuildRequest) -> Path:
    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)), autoescape=True)
    html = render_landing_page(env, request)
    request.output_path.parent.mkdir(parents=True, exist_ok=True)
    request.output_path.write_text(html, encoding="utf-8")
    return request.output_path


def parse_faq_items(raw_value: Optional[str]) -> List[Dict[str, str]]:
    if not raw_value:
        return []

    path = Path(raw_value)
    if path.exists():
        payload = path.read_text(encoding="utf-8")
    else:
        payload = raw_value

    parsed = yaml.safe_load(payload)
    if not isinstance(parsed, list):
        raise ValueError("FAQ items must decode to a list.")

    normalized: List[Dict[str, str]] = []
    for index, item in enumerate(parsed):
        if not isinstance(item, dict):
            raise ValueError(f"FAQ item at index {index} must be an object.")
        question = str(item.get("question", "")).strip()
        answer = str(item.get("answer", "")).strip()
        if not question or not answer:
            raise ValueError(f"FAQ item at index {index} requires question and answer.")
        normalized.append({"question": question, "answer": answer})
    return normalized


def render_landing_page(env: Environment, request: LandingBuildRequest) -> str:
    page_type = request.page_type
    if page_type not in LANDING_TEMPLATE_MAP:
        raise ValueError(f"Unsupported page type: {page_type}")

    context = build_context(request)
    html = env.get_template(LANDING_TEMPLATE_MAP[page_type]).render(**context)
    schema_blocks = build_schema_blocks(env, request, context)
    return inject_before_body_end(html, "\n".join(schema_blocks))


def build_context(request: LandingBuildRequest) -> dict[str, Any]:
    page_type = request.page_type
    slug = request.output_path.stem
    canonical_url = f"https://example.com/{slug}.html"
    title = resolve_title(request)
    meta_description = resolve_meta_description(request)
    faq_items = request.faq_items or []

    base_context: dict[str, Any] = {
        "brand_name": request.brand_name,
        "title": title,
        "meta_description": meta_description,
        "canonical_url": canonical_url,
        "home_url": "https://example.com/",
        "theme_js_url": "../site/assets/js/theme.js",
        "nav_items": [
            {"label": "Overview", "url": "https://example.com/"},
            {"label": "Tools", "url": "https://example.com/tools"},
            {"label": "Docs", "url": "https://example.com/docs"},
        ],
        "faq_items": faq_items,
        "breadcrumb": request.primary_keyword or "Article",
    }

    if page_type == "article":
        base_context.update(build_article_context(request))
    elif page_type == "c":
        base_context.update(build_type_c_context(request))
    else:
        base_context.update(build_conversion_context(request))

    return base_context


def build_conversion_context(request: LandingBuildRequest) -> dict[str, Any]:
    keyword = request.primary_keyword or ""
    value_prop = request.value_prop or f"Launch a production-ready experience for {keyword} without extra setup."

    return {
        "meta_line": value_prop,
        "insight_label": "Intent",
        "insight_title": "Search Opportunity",
        "metrics": [
            {"value": "24h", "label": "time to publish"},
            {"value": "SEO", "label": f"optimized for <strong>{keyword}</strong>", "class": "blue"},
            {"value": "FAQ", "label": f"{len(request.faq_items or [])} answer blocks", "class": "amber"},
            {"value": "Ready", "label": "static export compatible"},
        ],
        "boxes": [
            {
                "label": "Value Prop",
                "headline": value_prop,
                "text": f"{request.brand_name} packages product narrative, proof, and next-step CTA around the query {keyword}.",
            },
            {
                "label": "Use Case",
                "headline": f"Capture high-intent traffic for {keyword}",
                "text": "The page is structured for users who already know the problem and want a concrete product path.",
            },
        ],
        "entries": [
            {
                "label": "Primary CTA",
                "title": f"Start with {request.brand_name}",
                "desc": f"Use the guided flow to move from search query to usable output for {keyword}.",
                "chips": [{"text": "Launch", "class": "brand"}, {"text": "Guided", "class": "amber"}],
                "url": canonical_cta_url(request),
            },
            {
                "label": "Proof",
                "title": "See example outputs",
                "desc": "Reference examples, onboarding notes, and implementation details before committing.",
                "chips": [{"text": "Examples"}, {"text": "Docs"}],
                "url": "https://example.com/examples",
            },
        ],
        "extra_sections": build_faq_section(request.faq_items or []),
    }


def build_type_c_context(request: LandingBuildRequest) -> dict[str, Any]:
    keyword = request.primary_keyword or ""
    domain_data = {
        "streams": [
            {
                "id": "discover",
                "name": "Discovery",
                "tasks": [
                    {
                        "id": "query-map",
                        "status": "doing",
                        "priority": "P0",
                        "title": f"Map demand clusters for {keyword}",
                        "purpose": "Connect related search intents to usable entry pages.",
                        "definition": "Group head term, adjacent jobs, and comparison intents.",
                        "scope": "Search pages, docs, and examples.",
                        "outcome": "Hub can route users to the right sub-page quickly.",
                        "done_date": "",
                        "paths": [{"label": "Primary landing", "path": f"{request.output_path.name}"}],
                    },
                    {
                        "id": "cta-routing",
                        "status": "todo",
                        "priority": "P1",
                        "title": "Add routing hints for downstream tools",
                        "purpose": "Reduce pogo sticking from generic hub traffic.",
                        "definition": "Explain where each card leads and why.",
                        "scope": "Card copy and labels.",
                        "outcome": "Higher intent alignment.",
                        "done_date": "",
                        "paths": [{"label": "Examples", "path": "examples"}],
                    },
                ],
            }
        ]
    }
    return {
        "meta_line": f"Operational hub for {keyword} across discovery, routing, and activation.",
        "domain_data_json": json.dumps(domain_data, ensure_ascii=False, indent=2),
        "relative_root": "./",
    }


def build_article_context(request: LandingBuildRequest) -> dict[str, Any]:
    title = request.title or "Article"
    keyword = request.primary_keyword or title
    value_prop = request.value_prop or f"A practical breakdown of what matters about {keyword}."
    content = "\n".join(
        [
            f"<p>{value_prop}</p>",
            f"<h2>Why {keyword} matters</h2>",
            f"<p>{request.brand_name} can use this format to rank for information intent while pre-selling the product path.</p>",
            "<h2>What to include</h2>",
            "<ul><li>Specific workflow steps</li><li>Decision criteria</li><li>Links into product pages</li></ul>",
            "<h2>Next step</h2>",
            f"<p>Turn the strongest subsection into a dedicated conversion page once search demand stabilizes around {keyword}.</p>",
        ]
    )
    return {
        "breadcrumb": "Article",
        "category": "SEO Article",
        "author": request.brand_name,
        "publish_date": "2026-06-30",
        "read_time": "6 min read",
        "content": content,
        "related": [
            {"title": "Product Page", "url": canonical_cta_url(request)},
            {"title": "Examples", "url": "https://example.com/examples"},
        ],
    }


def build_schema_blocks(env: Environment, request: LandingBuildRequest, context: dict[str, Any]) -> list[str]:
    blocks: list[str] = []
    if request.page_type in {"a", "b", "c"}:
        blocks.append(
            env.get_template("components/webapp-schema.html").render(
                app_name=context["title"],
                app_description=context["meta_description"],
                app_category="BusinessApplication" if request.page_type == "c" else "MultimediaApplication",
                canonical_url=context["canonical_url"],
            )
        )
    if context.get("faq_items"):
        blocks.append(env.get_template("components/faq-schema.html").render(faq_items=context["faq_items"]))
    if request.page_type == "article":
        blocks.append(render_article_schema(context))
    return blocks


def render_article_schema(context: dict[str, Any]) -> str:
    payload = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": context["title"],
        "description": context["meta_description"],
        "author": {"@type": "Organization", "name": context["author"]},
        "datePublished": context["publish_date"],
        "mainEntityOfPage": context["canonical_url"],
    }
    return '<script type="application/ld+json">\n' + json.dumps(payload, ensure_ascii=False, indent=2) + "\n</script>"


def inject_before_body_end(html: str, block: str) -> str:
    if "</body>" not in html:
        return html + "\n" + block
    return html.replace("</body>", f"{block}\n</body>", 1)


def resolve_title(request: LandingBuildRequest) -> str:
    if request.page_type == "article":
        return request.title or "Article"
    return request.primary_keyword or "Landing Page"


def resolve_meta_description(request: LandingBuildRequest) -> str:
    keyword = request.primary_keyword or request.title or "growth workflow"
    if request.value_prop:
        return request.value_prop
    return f"{request.brand_name} helps users move from query to usable outcome for {keyword}."


def build_faq_section(faq_items: list[dict[str, str]]) -> str:
    if not faq_items:
        return ""
    parts = [
        '<section class="sec" id="faq">',
        '<div class="sec-head"><span class="num">FAQ</span><h2>Common Questions</h2></div>',
    ]
    for item in faq_items:
        parts.append(
            '<div class="box" style="padding:18px;margin-bottom:12px">'
            f'<div style="font-size:14px;font-weight:900;margin-bottom:8px">{item["question"]}</div>'
            f'<p style="margin:0;font-size:13px;color:var(--muted)">{item["answer"]}</p>'
            "</div>"
        )
    parts.append("</section>")
    return "".join(parts)


def canonical_cta_url(request: LandingBuildRequest) -> str:
    slug = request.output_path.stem
    return f"https://example.com/{slug}.html#start"
