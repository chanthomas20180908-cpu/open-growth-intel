from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer

from cli.landing_builder import LandingBuildRequest, build_landing_page, parse_faq_items


app = typer.Typer(help="Open Growth Intelligence CLI")
landing_app = typer.Typer(help="Build SEO/GEO landing pages.")
app.add_typer(landing_app, name="landing")


@landing_app.command("build")
def landing_build(
    page_type: str = typer.Option(..., "--type", help="Page type: a, b, c, article."),
    brand: str = typer.Option(..., "--brand", help="Brand name."),
    output: Path = typer.Option(..., "--output", help="Output HTML path."),
    keyword: Optional[str] = typer.Option(None, "--keyword", help="Primary keyword for type a/b/c."),
    title: Optional[str] = typer.Option(None, "--title", help="Article title."),
    value_prop: Optional[str] = typer.Option(None, "--value-prop", help="One-line value proposition."),
    faq_items: Optional[str] = typer.Option(None, "--faq-items", help="FAQ items as JSON/YAML string or file path."),
) -> None:
    normalized_type = page_type.lower().strip()
    if normalized_type not in {"a", "b", "c", "article"}:
        raise typer.BadParameter("Page type must be one of: a, b, c, article.", param_hint="--type")
    if normalized_type == "article" and not title:
        raise typer.BadParameter("Article pages require --title.", param_hint="--title")
    if normalized_type in {"a", "b", "c"} and not keyword:
        raise typer.BadParameter("Type a/b/c pages require --keyword.", param_hint="--keyword")

    try:
        parsed_faq_items = parse_faq_items(faq_items)
    except ValueError as exc:
        raise typer.BadParameter(str(exc), param_hint="--faq-items") from exc

    request = LandingBuildRequest(
        page_type=normalized_type,
        brand_name=brand.strip(),
        primary_keyword=keyword.strip() if keyword else None,
        title=title.strip() if title else None,
        output_path=output,
        value_prop=value_prop.strip() if value_prop else None,
        faq_items=parsed_faq_items,
    )
    output_path = build_landing_page(request)
    typer.echo(f"Built landing page: {output_path}")


if __name__ == "__main__":
    app()
