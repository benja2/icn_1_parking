#!/usr/bin/env python3
"""Fetch Incheon Airport T1 parking availability and publish it to ntfy."""

from __future__ import annotations

import html
import re
import subprocess


AIRPORT_URL = "https://business.airport.kr/ap_ko/index.do"
NTFY_URL = "https://ntfy.sh/icn-parking-e7c05cfe-d92d-445c-8916-c49b767b749f"


def fetch_page() -> str:
    result = subprocess.run(
        [
            "curl",
            "--fail",
            "--location",
            "--silent",
            "--show-error",
            "--max-time",
            "30",
            "--user-agent",
            "Mozilla/5.0 (compatible; ICNParkingMonitor/1.0)",
            AIRPORT_URL,
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def extract_value(page: str, label: str) -> str:
    pattern = rf"<strong>{re.escape(label)}</strong>(.*?)(?=</li>)"
    match = re.search(pattern, page, flags=re.DOTALL)
    if not match:
        raise ValueError(f"Parking entry not found: {label}")

    section = match.group(1)
    if "만차" in section:
        return "만차"

    count = re.search(r"<i>\s*([0-9,]+)\s*</i>\s*대 가능", section)
    if not count:
        raise ValueError(f"Availability not found: {label}")
    return f"{count.group(1)}대 가능"


def build_message(page: str) -> str:
    values = {
        "p1_long": extract_value(page, "장기주차장 P1"),
        "p1_tower": extract_value(page, "주차타워 동편"),
        "p2_long": extract_value(page, "장기주차 P2"),
        "p2_tower": extract_value(page, "주차타워 서편"),
    }
    return (
        f"P1 | 장기주차장: {values['p1_long']} | 주차타워: {values['p1_tower']}\n"
        f"P2 | 장기주차장: {values['p2_long']} | 주차타워: {values['p2_tower']}"
    )


def publish(message: str) -> None:
    subprocess.run(
        [
            "curl",
            "--fail",
            "--location",
            "--silent",
            "--show-error",
            "--max-time",
            "30",
            "--header",
            "Title: Incheon Airport T1 Parking",
            "--header",
            "Tags: parking",
            "--data-binary",
            "@-",
            NTFY_URL,
        ],
        input=message,
        check=True,
        text=True,
    )


def main() -> None:
    page = html.unescape(fetch_page())
    message = build_message(page)
    print(message)
    publish(message)


if __name__ == "__main__":
    main()
