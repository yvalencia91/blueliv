from datetime import datetime


def format_date(post_date: str) -> str:
    pretty_date = datetime.strptime(post_date, "%B %d, %Y").strftime("%Y-%m-%d")
    return pretty_date
