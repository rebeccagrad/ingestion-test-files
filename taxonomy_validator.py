# Taxonomy validation utilities for content ingestion

def validate_tags(tags):
    return [tag.strip() for tag in tags if tag.strip()]

def apply_taxonomy(article, tags):
    article["tags"] = validate_tags(tags)
    return article

def check_missing_tags(articles):
    return [a for a in articles if not a.get("tags")]

